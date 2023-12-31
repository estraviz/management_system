# Generated by Django 4.2.4 on 2023-08-27 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("todo_dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("avatar", models.ImageField(blank=True, upload_to="photos/")),
                ("department", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ToDoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("label", models.CharField(blank=True, max_length=128)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("due_date", models.DateTimeField(blank=True, null=True)),
                (
                    "time_estimate_hours",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("comment", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "dashboard_column",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todo_dashboard.dashboardcolumn",
                    ),
                ),
                (
                    "subtask_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todo_dashboard.todoitem",
                    ),
                ),
            ],
            options={
                "verbose_name": "ToDo Item",
                "verbose_name_plural": "ToDo Items",
            },
        ),
        migrations.AddField(
            model_name="dashboardcolumn",
            name="dashboard",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="todo_dashboard.dashboard",
            ),
        ),
        migrations.AddField(
            model_name="dashboard",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="member",
                to="todo_dashboard.member",
            ),
        ),
    ]
