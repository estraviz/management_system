from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class TodoDashboardConfig(AppConfig):
    name = 'todo_dashboard'
    verbose_name = "Todo Dashboard"


class MyAdminConfig(AdminConfig):
    default_site = 'todo_dashboard.admin.MyAdminSite'
