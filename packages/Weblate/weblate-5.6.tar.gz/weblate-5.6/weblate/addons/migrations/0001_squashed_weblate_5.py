# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-09-18 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("addons", "0001_squashed_0021_linguas_daily"),
        ("addons", "0002_cleanup_addon_events"),
        ("addons", "0003_alter_event_event"),
        ("addons", "0004_addon_configuration_new_addon_state_new"),
        ("addons", "0005_jsonfield"),
        ("addons", "0006_remove_addon_configuration_remove_addon_state"),
        ("addons", "0007_rename_configuration_new_addon_configuration_and_more"),
        ("addons", "0008_alter_event_addon"),
    ]

    initial = True

    dependencies = [
        ("trans", "0001_squashed_weblate_5"),
    ]

    operations = [
        migrations.CreateModel(
            name="Addon",
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
                ("name", models.CharField(max_length=100)),
                (
                    "component",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.component",
                    ),
                ),
                ("project_scope", models.BooleanField(db_index=True, default=False)),
                ("repo_scope", models.BooleanField(db_index=True, default=False)),
                ("configuration", models.JSONField(default=dict)),
                ("state", models.JSONField(default=dict)),
            ],
            options={
                "verbose_name": "add-on",
                "verbose_name_plural": "add-ons",
            },
        ),
        migrations.CreateModel(
            name="Event",
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
                    "event",
                    models.IntegerField(
                        choices=[
                            (1, "repository post-push"),
                            (2, "repository post-update"),
                            (3, "repository pre-commit"),
                            (4, "repository post-commit"),
                            (5, "repository post-add"),
                            (6, "unit post-create"),
                            (7, "storage post-load"),
                            (8, "unit post-save"),
                            (9, "repository pre-update"),
                            (10, "repository pre-push"),
                            (11, "daily"),
                            (12, "component update"),
                        ]
                    ),
                ),
                (
                    "addon",
                    models.ForeignKey(
                        db_index=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="addons.addon",
                    ),
                ),
            ],
            options={
                "unique_together": {("addon", "event")},
                "verbose_name": "add-on event",
                "verbose_name_plural": "add-on events",
            },
        ),
    ]
