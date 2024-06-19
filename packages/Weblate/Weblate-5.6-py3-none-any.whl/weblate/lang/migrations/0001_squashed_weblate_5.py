# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-09-18 08:18

import django.db.models.deletion
from django.db import migrations, models

import weblate.lang.models
import weblate.utils.validators


class Migration(migrations.Migration):
    replaces = [
        ("lang", "0001_squashed_0008_auto_20200408_0436"),
        ("lang", "0009_auto_20200521_0753"),
        ("lang", "0010_auto_20200627_0508"),
        ("lang", "0011_alter_plural_source"),
        ("lang", "0012_alter_plural_type"),
        ("lang", "0013_alter_plural_formula"),
        ("lang", "0014_language_population"),
        ("lang", "0015_population"),
        ("lang", "0016_alter_plural_source"),
        ("lang", "0017_alter_plural_type"),
        ("lang", "0018_alter_plural_type"),
        ("lang", "0019_alter_plural_type"),
        ("lang", "0020_alter_plural_source"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.SlugField(unique=True, verbose_name="Language code")),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Language name"),
                ),
                (
                    "direction",
                    models.CharField(
                        choices=[
                            ("", ""),
                            ("ltr", "Left to right"),
                            ("rtl", "Right to left"),
                        ],
                        default="",
                        max_length=3,
                        verbose_name="Text direction",
                    ),
                ),
                (
                    "population",
                    models.BigIntegerField(
                        default=0,
                        help_text="Number of people speaking this language.",
                        verbose_name="Number of speakers",
                    ),
                ),
            ],
            options={
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
                "base_manager_name": "objects",
            },
            managers=[
                ("objects", weblate.lang.models.LanguageManager()),
            ],
        ),
        migrations.CreateModel(
            name="Plural",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "source",
                    models.SmallIntegerField(
                        choices=[
                            (0, "Default plural"),
                            (1, "gettext plural formula"),
                            (3, "CLDR plural with zero"),
                            (4, "CLDR v38+ plural"),
                            (5, "Android plural"),
                            (2, "Manually entered formula"),
                        ],
                        default=0,
                        verbose_name="Plural definition source",
                    ),
                ),
                (
                    "number",
                    models.SmallIntegerField(
                        default=2, verbose_name="Number of plurals"
                    ),
                ),
                (
                    "formula",
                    models.TextField(
                        default="n != 1",
                        validators=[weblate.utils.validators.validate_plural_formula],
                        verbose_name="Plural formula",
                    ),
                ),
                (
                    "type",
                    models.IntegerField(
                        choices=[
                            (0, "None"),
                            (1, "One/other"),
                            (2, "One/few/other"),
                            (3, "Arabic languages"),
                            (11, "Zero/one/other"),
                            (4, "One/two/other"),
                            (14, "One/other/two"),
                            (6, "One/two/few/other"),
                            (13, "Other/one/two/few"),
                            (5, "One/two/three/other"),
                            (7, "One/other/zero"),
                            (8, "One/few/many/other"),
                            (9, "Two/other"),
                            (10, "One/two/few/many/other"),
                            (12, "Zero/one/two/few/many/other"),
                            (15, "Zero/other"),
                            (16, "Zero/one/few/other"),
                            (17, "Zero/one/two/few/other"),
                            (18, "Zero/one/two/other"),
                            (19, "Zero/one/few/many/other"),
                            (20, "One/many/other"),
                            (21, "Zero/one/many/other"),
                            (22, "One/few/many"),
                            (666, "Unknown"),
                        ],
                        default=666,
                        editable=False,
                        verbose_name="Plural type",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lang.language"
                    ),
                ),
            ],
            options={
                "verbose_name": "Plural form",
                "verbose_name_plural": "Plural forms",
            },
        ),
    ]
