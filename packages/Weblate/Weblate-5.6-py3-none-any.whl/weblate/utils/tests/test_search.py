# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import datetime, timedelta, timezone

from django.db.models import Q
from django.test import SimpleTestCase, TestCase

from weblate.auth.models import User
from weblate.trans.models import Change, Unit
from weblate.trans.tests.test_views import ViewTestCase
from weblate.trans.util import PLURAL_SEPARATOR
from weblate.utils.db import using_postgresql
from weblate.utils.search import Comparer, parse_query
from weblate.utils.state import (
    STATE_APPROVED,
    STATE_EMPTY,
    STATE_FUZZY,
    STATE_READONLY,
    STATE_TRANSLATED,
)


class ComparerTest(SimpleTestCase):
    def test_different(self) -> None:
        self.assertLessEqual(Comparer().similarity("a", "b"), 50)

    def test_same(self) -> None:
        self.assertEqual(Comparer().similarity("a", "a"), 100)

    def test_unicode(self) -> None:
        # Test fallback to Python implementation in jellyfish
        # for unicode strings
        self.assertEqual(Comparer().similarity("NICHOLASŸ", "NICHOLAS"), 88)


class SearchMixin:
    object_class = Unit
    parser = "unit"

    def assert_query(self, string, expected, exists=False, **context) -> None:
        result = parse_query(string, parser=self.parser, **context)
        self.assertEqual(result, expected)
        self.assertEqual(self.object_class.objects.filter(result).exists(), exists)


class UnitQueryParserTest(TestCase, SearchMixin):
    def test_simple(self) -> None:
        self.assert_query(
            "hello world",
            (
                Q(source__substring="hello")
                | Q(target__substring="hello")
                | Q(context__substring="hello")
            )
            & (
                Q(source__substring="world")
                | Q(target__substring="world")
                | Q(context__substring="world")
            ),
        )

    def test_quote(self) -> None:
        expected = (
            Q(source__substring="hello world")
            | Q(target__substring="hello world")
            | Q(context__substring="hello world")
        )
        self.assert_query('"hello world"', expected)
        self.assert_query("'hello world'", expected)

    def test_context(self) -> None:
        expected = Q(context__substring="hello world")
        self.assert_query('key:"hello world"', expected)
        self.assert_query("context:'hello world'", expected)

    def test_text(self) -> None:
        self.assert_query("note:TEXT", Q(note__substring="TEXT"))
        self.assert_query("location:TEXT", Q(location__substring="TEXT"))

    def test_newline(self) -> None:
        self.assert_query("location:TEXT\r\n", Q(location__substring="TEXT"))
        self.assert_query("location:TEXT\r", Q(location__substring="TEXT"))
        self.assert_query("location:TEXT\n", Q(location__substring="TEXT"))
        self.assert_query("location:'TEXT'\r\n", Q(location__substring="TEXT"))

    def test_comment(self) -> None:
        self.assert_query(
            "comment:TEXT",
            Q(comment__comment__substring="TEXT") & Q(comment__resolved=False),
        )
        self.assert_query(
            "resolved_comment:TEXT",
            Q(comment__comment__substring="TEXT") & Q(comment__resolved=True),
        )
        self.assert_query(
            "comment_author:nijel", Q(comment__user__username__iexact="nijel")
        )

    def test_field(self) -> None:
        self.assert_query(
            "source:hello target:world",
            Q(source__substring="hello") & Q(target__substring="world"),
        )
        self.assert_query("location:hello.c", Q(location__substring="hello.c"))

    def test_exact(self) -> None:
        self.assert_query("source:='hello'", Q(source__exact="hello"))
        self.assert_query('source:="hello world"', Q(source__exact="hello world"))
        self.assert_query("source:='hello world'", Q(source__exact="hello world"))
        self.assert_query("source:=hello", Q(source__exact="hello"))

    def test_regex(self) -> None:
        self.assert_query('source:r"^hello"', Q(source__trgm_regex="^hello"))
        # Invalid regex
        with self.assertRaises(ValueError):
            self.assert_query('source:r"^(hello"', Q(source__trgm_regex="^(hello"))
        # Not supported regex on PostgreSQL
        with self.assertRaises(ValueError):
            self.assert_query(
                'source:r"^(?i)hello"', Q(source__trgm_regex="^(?i)hello")
            )
        self.assert_query('source:r"(?i)^hello"', Q(source__trgm_regex="(?i)^hello"))

    def test_logic(self) -> None:
        self.assert_query(
            "source:hello AND NOT target:world",
            Q(source__substring="hello") & ~Q(target__substring="world"),
        )
        self.assert_query(
            "source:hello OR target:world",
            Q(source__substring="hello") | Q(target__substring="world"),
        )

    def test_empty(self) -> None:
        self.assert_query("", Q())

    def test_invalid(self) -> None:
        with self.assertRaises(ValueError):
            self.assert_query(
                "changed:inval AND target:world", Q(target__substring="world")
            )

    def test_year(self) -> None:
        self.assert_query(
            "changed:2018",
            Q(
                change__timestamp__range=(
                    datetime(2018, 1, 1, 0, 0, tzinfo=timezone.utc),
                    datetime(2018, 12, 31, 23, 59, 59, 999999, tzinfo=timezone.utc),
                )
            )
            & Q(change__action__in=Change.ACTIONS_CONTENT),
        )

    def test_change_action(self) -> None:
        expected = Q(
            change__timestamp__range=(
                datetime(2018, 1, 1, 0, 0, tzinfo=timezone.utc),
                datetime(2018, 12, 31, 23, 59, 59, 999999, tzinfo=timezone.utc),
            )
        ) & Q(change__action=Change.ACTION_MARKED_EDIT)
        self.assert_query(
            "change_time:2018 AND change_action:marked-for-edit", expected
        )
        self.assert_query(
            "change_time:2018 AND change_action:'Marked for edit'", expected
        )

    def test_dates(self) -> None:
        action_change = Q(change__action__in=Change.ACTIONS_CONTENT)
        self.assert_query(
            "changed:>20190301",
            Q(change__timestamp__gte=datetime(2019, 3, 1, 0, 0, tzinfo=timezone.utc))
            & action_change,
        )
        self.assert_query(
            "changed:>2019-03-01",
            Q(change__timestamp__gte=datetime(2019, 3, 1, 0, 0, tzinfo=timezone.utc))
            & action_change,
        )
        self.assert_query(
            "changed:2019-03-01",
            Q(
                change__timestamp__range=(
                    datetime(2019, 3, 1, 0, 0, tzinfo=timezone.utc),
                    datetime(2019, 3, 1, 23, 59, 59, 999999, tzinfo=timezone.utc),
                )
            )
            & action_change,
        )
        with self.assertRaises(ValueError):
            self.assert_query("changed:>=2010-01-", Q())

    def test_date_range(self) -> None:
        self.assert_query(
            "changed:[2019-03-01 to 2019-04-01]",
            Q(
                change__timestamp__range=(
                    datetime(2019, 3, 1, 0, 0, tzinfo=timezone.utc),
                    datetime(2019, 4, 1, 23, 59, 59, 999999, tzinfo=timezone.utc),
                )
            )
            & Q(change__action__in=Change.ACTIONS_CONTENT),
        )

    def test_date_added(self) -> None:
        self.assert_query(
            "added:>2019-03-01",
            Q(timestamp__gte=datetime(2019, 3, 1, 0, 0, tzinfo=timezone.utc)),
        )

    def test_source_changed(self) -> None:
        self.assert_query(
            "source_changed:>20190301",
            Q(
                source_unit__last_updated__gte=datetime(
                    2019, 3, 1, 0, 0, tzinfo=timezone.utc
                )
            ),
        )

    def test_bool(self) -> None:
        self.assert_query("pending:true", Q(pending=True))

    def test_nonexisting(self) -> None:
        with self.assertRaises(ValueError):
            self.assert_query("nonexisting:true", Q())

    def test_state(self) -> None:
        self.assert_query("state:>=empty", Q(state__gte=STATE_EMPTY))
        self.assert_query("state:>=translated", Q(state__gte=STATE_TRANSLATED))
        self.assert_query("state:<translated", Q(state__lt=STATE_TRANSLATED))
        self.assert_query("state:translated", Q(state=STATE_TRANSLATED))
        self.assert_query("state:needs-editing", Q(state=STATE_FUZZY))

    def test_position(self) -> None:
        self.assert_query("position:>=1", Q(position__gte=1))
        self.assert_query("position:<10", Q(position__lt=10))
        self.assert_query("position:[1 to 10]", Q(position__range=(1, 10)))

    def test_invalid_state(self) -> None:
        with self.assertRaises(ValueError):
            self.assert_query("state:invalid", Q())

    def test_parenthesis(self) -> None:
        self.assert_query(
            "state:translated AND ( source:hello OR source:bar )",
            Q(state=STATE_TRANSLATED)
            & (Q(source__substring="hello") | Q(source__substring="bar")),
        )
        self.assert_query(
            "state:translated AND (source:hello OR source:bar)",
            Q(state=STATE_TRANSLATED)
            & (Q(source__substring="hello") | Q(source__substring="bar")),
        )

    def test_language(self) -> None:
        self.assert_query("language:cs", Q(translation__language__code__iexact="cs"))
        self.assert_query(
            'language:r".*"', Q(translation__language__code__trgm_regex=".*")
        )

    def test_component(self) -> None:
        self.assert_query(
            "component:hello",
            Q(translation__component__slug__iexact="hello")
            | Q(translation__component__name__icontains="hello"),
        )

    def test_project(self) -> None:
        self.assert_query(
            "project:hello", Q(translation__component__project__slug__iexact="hello")
        )

    def test_html(self) -> None:
        self.assert_query(
            "<b>bold</b>",
            Q(source__substring="<b>bold</b>")
            | Q(target__substring="<b>bold</b>")
            | Q(context__substring="<b>bold</b>"),
        )

    def test_has(self) -> None:
        self.assert_query("has:plural", Q(source__search=PLURAL_SEPARATOR))
        self.assert_query("has:suggestion", Q(suggestion__isnull=False))
        self.assert_query("has:check", Q(check__dismissed=False))
        self.assert_query("has:comment", Q(comment__resolved=False))
        self.assert_query("has:note", ~Q(note=""))
        self.assert_query("has:resolved-comment", Q(comment__resolved=True))
        self.assert_query("has:dismissed-check", Q(check__dismissed=True))
        self.assert_query("has:translation", Q(state__gte=STATE_TRANSLATED))
        self.assert_query("has:variant", Q(variant__isnull=False))
        self.assert_query(
            "has:label", Q(source_unit__labels__isnull=False) | Q(labels__isnull=False)
        )
        self.assert_query("has:context", ~Q(context=""))
        self.assert_query(
            "has:screenshot",
            Q(screenshots__isnull=False) | Q(source_unit__screenshots__isnull=False),
        )
        self.assert_query("has:flags", ~Q(source_unit__extra_flags=""))
        self.assert_query("has:explanation", ~Q(source_unit__explanation=""))
        self.assert_query("has:glossary", Q(source__isnull=True))

    def test_is(self) -> None:
        self.assert_query("is:pending", Q(pending=True))
        self.assert_query("is:translated", Q(state__gte=STATE_TRANSLATED))
        self.assert_query("is:untranslated", Q(state__lt=STATE_TRANSLATED))
        self.assert_query("is:approved", Q(state=STATE_APPROVED))
        self.assert_query("is:read-only", Q(state=STATE_READONLY))
        self.assert_query("is:fuzzy", Q(state=STATE_FUZZY))

    def test_changed_by(self) -> None:
        self.assert_query(
            "changed_by:nijel",
            Q(change__author__username__iexact="nijel")
            & Q(change__action__in=Change.ACTIONS_CONTENT),
        )

    def test_explanation(self) -> None:
        self.assert_query(
            "explanation:text", Q(source_unit__explanation__substring="text")
        )

    def test_suggestions(self) -> None:
        self.assert_query("suggestion:text", Q(suggestion__target__substring="text"))
        self.assert_query(
            "suggestion_author:nijel", Q(suggestion__user__username__iexact="nijel")
        )

    def test_checks(self) -> None:
        self.assert_query(
            "check:ellipsis",
            Q(check__name__iexact="ellipsis") & Q(check__dismissed=False),
        )
        self.assert_query(
            "dismissed_check:ellipsis",
            Q(check__name__iexact="ellipsis") & Q(check__dismissed=True),
        )

    def test_labels(self) -> None:
        self.assert_query(
            "label:'test label'",
            Q(source_unit__labels__name__iexact="test label")
            | Q(labels__name__iexact="test label"),
        )

    def test_screenshot(self) -> None:
        self.assert_query(
            "screenshot:'test screenshot'",
            Q(source_unit__screenshots__name__iexact="test screenshot")
            | Q(screenshots__name__iexact="test screenshot"),
        )

    def test_priority(self) -> None:
        self.assert_query("priority:10", Q(priority=10))
        self.assert_query("priority:>=10", Q(priority__gte=10))

    def test_id(self) -> None:
        self.assert_query("id:100", Q(id=100))
        self.assert_query("id:100,900", Q(id__in={100, 900}))

    def test_text_html(self) -> None:
        self.assert_query("target:<name>", Q(target__substring="<name>"))

    def test_text_long(self) -> None:
        self.assert_query(
            "[one to other]",
            (
                Q(source__substring="[one")
                | Q(target__substring="[one")
                | Q(context__substring="[one")
            )
            & (
                Q(source__substring="to")
                | Q(target__substring="to")
                | Q(context__substring="to")
            )
            & (
                Q(source__substring="other]")
                | Q(target__substring="other]")
                | Q(context__substring="other]")
            ),
        )

    def test_lowercase_or(self) -> None:
        self.assert_query(
            "state:<translated or state:empty",
            Q(state__lt=STATE_TRANSLATED) | Q(state=STATE_EMPTY),
        )

    def test_timestamp_format(self) -> None:
        self.assert_query(
            "changed:>=01/20/2020",
            Q(change__timestamp__gte=datetime(2020, 1, 20, 0, 0, tzinfo=timezone.utc))
            & Q(change__action__in=Change.ACTIONS_CONTENT),
        )

    def test_timestamp_interval(self) -> None:
        self.assert_query(
            "changed:2020-03-27",
            Q(
                change__timestamp__range=(
                    datetime(2020, 3, 27, 0, 0, tzinfo=timezone.utc),
                    datetime(2020, 3, 27, 23, 59, 59, 999999, tzinfo=timezone.utc),
                )
            )
            & Q(change__action__in=Change.ACTIONS_CONTENT),
        )

    def test_non_quoted_strings(self) -> None:
        self.assert_query(
            "%(count)s word",
            parse_query("'%(count)s' 'word'"),
        )
        self.assert_query("{actor}", parse_query("'{actor}'"))

    def test_specialchars(self) -> None:
        self.assert_query(
            "to %{_topdir}",
            (
                Q(source__substring="to")
                | Q(target__substring="to")
                | Q(context__substring="to")
            )
            & (
                Q(source__substring="%{_topdir}")
                | Q(target__substring="%{_topdir}")
                | Q(context__substring="%{_topdir}")
            ),
        )

    def test_url(self) -> None:
        self.assert_query("https://weblate.org/", parse_query("'https://weblate.org/'"))

    def test_quotes(self) -> None:
        self.assert_query("'", parse_query('''"'"'''))
        self.assert_query('"', parse_query("""'"'"""))
        self.assert_query("source:'", parse_query('''source:"'"'''))
        self.assert_query('source:"', parse_query("""source:'"'"""))


class UserQueryParserTest(TestCase, SearchMixin):
    object_class = User
    parser = "user"

    def test_simple(self) -> None:
        self.assert_query(
            "hello",
            Q(username__icontains="hello") | Q(full_name__icontains="hello"),
        )

    def test_fields(self) -> None:
        self.assert_query(
            "username:hello",
            Q(username__icontains="hello"),
        )
        self.assert_query(
            "full_name:hello",
            Q(full_name__icontains="hello"),
        )

    def test_is(self) -> None:
        with self.assertRaises(ValueError):
            self.assert_query("is:bot", Q(is_bot=True))
        with self.assertRaises(ValueError):
            self.assert_query("is:superuser", Q(is_superuser=True))
        with self.assertRaises(ValueError):
            self.assert_query("is:active", Q(is_active=True))

    def test_language(self) -> None:
        self.assert_query("language:cs", (Q(profile__languages__code__iexact="cs")))

    def test_email(self) -> None:
        with self.assertRaises(ValueError):
            self.assert_query(
                "email:hello",
                Q(social_auth__verifiedemail__email__icontains="hello"),
            )

    def test_joined(self) -> None:
        self.assert_query(
            "joined:2018",
            Q(
                date_joined__range=(
                    datetime(2018, 1, 1, 0, 0, tzinfo=timezone.utc),
                    datetime(2018, 12, 31, 23, 59, 59, 999999, tzinfo=timezone.utc),
                )
            ),
        )

    def test_translates(self) -> None:
        self.assert_query(
            "translates:cs",
            Q(change__language__code__iexact="cs")
            & Q(
                change__timestamp__date__gte=datetime.now(tz=timezone.utc).date()
                - timedelta(days=30)
            ),
        )

    def test_contributes(self) -> None:
        self.assert_query(
            "contributes:test",
            Q(change__project__slug__iexact="test")
            & Q(
                change__timestamp__date__gte=datetime.now(tz=timezone.utc).date()
                - timedelta(days=30)
            ),
        )
        self.assert_query(
            "contributes:test/test",
            Q(change__component_id__in=[])
            & Q(
                change__timestamp__date__gte=datetime.now(tz=timezone.utc).date()
                - timedelta(days=30)
            ),
        )


class SuperuserQueryParserTest(UserQueryParserTest):
    parser = "superuser"

    def test_simple(self) -> None:
        self.assert_query(
            "hello",
            (
                Q(username__icontains="hello")
                | Q(full_name__icontains="hello")
                | Q(social_auth__verifiedemail__email__iexact="hello")
            ),
        )

    def test_email(self) -> None:
        self.assert_query(
            "email:hello", Q(social_auth__verifiedemail__email__icontains="hello")
        )

    def test_is(self) -> None:
        self.assert_query("is:bot", Q(is_bot=True))
        self.assert_query("is:superuser", Q(is_superuser=True))
        self.assert_query("is:active", Q(is_active=True))


class SearchTest(ViewTestCase, SearchMixin):
    """Search tests on real projects."""

    CREATE_GLOSSARIES: bool = True

    def test_glossary_empty(self) -> None:
        self.assert_query("has:glossary", Q(source__isnull=True), project=self.project)

    def test_glossary_match(self) -> None:
        glossary = self.project.glossaries[0].translation_set.get(language_code="cs")
        glossary.add_unit(None, "", "hello", "ahoj")

        if using_postgresql():
            expected = "[[:<:]](hello)[[:>:]]"
        else:
            expected = r"(^|[ \t\n\r\f\v])(hello)($|[ \t\n\r\f\v])"
        self.assert_query(
            "has:glossary",
            Q(source__iregex=expected),
            True,
            project=self.project,
        )
