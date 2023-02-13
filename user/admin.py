from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import CustomUser
from .resources import UserResource


class NewUserAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = UserResource

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'
    list_display = ('username', 'email', 'last_name', 'is_staff', 'group')
    list_filter = ('username', 'email', 'last_name',)


# Register your models here.


admin.site.register(CustomUser, NewUserAdmin)
