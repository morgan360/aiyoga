from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Poses, PoseType


class PoseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'sanskrit_name']
    list_filter = ['name']


class PoseTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Poses, PoseAdmin)
admin.site.register(PoseType, PoseTypeAdmin)
