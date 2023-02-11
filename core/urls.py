from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ai.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += staticfiles_urlpatterns()
