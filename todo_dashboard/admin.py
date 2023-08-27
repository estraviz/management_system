from typing import Any, List, Tuple

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Dashboard, DashboardColumn, Member, ToDoItem


class DashboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_owner', 'created_at', 'updated_at',
                    'is_public')
    list_display_links = ('id', 'title')
    list_editable = ('is_public',)

    # def get_list_display(self, record) -> list[str]:
    #     list_display = ['id', 'title', 'get_owner', 'is_public']

    #     if record.user.is_superuser:
    #         list_display += ['created_at', 'updated_at']

    #     return list_display

    def get_owner(self, record):
        return record.owner.user.username

    get_owner.short_description = "Owner"


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('title', 'dashboard', 'created_at', 'updated_at')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'created_at', 'updated_at',
                    'get_avatar')

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="75" />')
        else:
            return '-'

    get_avatar.short_description = "THUMBNAIL"
    empty_value_display = 'UNSET'


class TodoItemFilter(admin.SimpleListFilter):
    title = 'Difficulty'
    parameter_name = 'time_estimate_hours'

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return (
            ('easy', 'Easy'),
            ('average', 'Average'),
            ('hard', 'Hard'),
        )

    def queryset(self, request: Any, queryset: Any) -> Any:
        if self.value() == 'easy':
            return queryset.filter(time_estimate_hours__lt=2)
        elif self.value() == 'average':
            return queryset.filter(time_estimate_hours__gte=2,
                                   time_estimate_hours__lte=8)
        elif self.value() == 'hard':
            return queryset.filter(time_estimate_hours__gt=8)


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'label', 'comment', 'due_date',
                    'time_estimate_hours',)
    list_editable = ('label', 'time_estimate_hours')

    search_fields = ('description', 'comment')
    list_filter = ('label', TodoItemFilter,)

    sortable_by = ('label', 'due_date', 'time_estimate_hours',)
    ordering = ('due_date', 'time_estimate_hours')

    actions_on_bottom = True


admin.site.register(Member, MemberAdmin)
admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(DashboardColumn, ColumnAdmin)
admin.site.register(ToDoItem, ToDoItemAdmin)

admin.site.site_header = "ADMIN PANEL"
admin.site.site_title = "SITE ADMIN"
admin.site.index_title = "ADMINISTRATION"
