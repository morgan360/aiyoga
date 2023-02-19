from django.contrib import admin
from .models import YogaImage
from django.utils.html import format_html


# @admin.register(YogaImage)
class YogaImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_filter = ['title']
    # readonly_fields = ['image']

    def image_preview(self, obj):
        return format_html('<img src="{}" height="50" />'.format(obj.image.url))

    image_preview.short_description = 'Image'


admin.site.register(YogaImage, YogaImageAdmin)
