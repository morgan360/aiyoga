from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Poses, PoseType
from django_summernote.admin import SummernoteModelAdmin


# class PoseAdmin(ImportExportMixin, admin.ModelAdmin,SummernoteModelAdmin ):
#     list_display = ['name', 'sanskrit_name']
#     list_filter = ['name']
#     summernote_fields = '__All__'

class PoseTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']


class SummerAdmin(ImportExportMixin, SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ['instructions', 'tips']
    list_display = ['name', 'sanskrit_name']
    list_filter = ['name']


admin.site.register(Poses, SummerAdmin)
admin.site.register(PoseType, PoseTypeAdmin)
# admin.site.register(Poses, SummerAdmin)
