from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth
    path('pose/', include('poses.urls')),
    path('display/', include('display.urls')),
    path('', include('ai.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

# urlpatterns += staticfiles_urlpatterns()
