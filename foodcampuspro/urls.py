from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static  


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage_view, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('menu/', include('menus.urls')),
    path('reservations/', include('reservations.urls')),
    # path('categories/', include('categories.urls')),  # Removed because the app was deleted
]


# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    