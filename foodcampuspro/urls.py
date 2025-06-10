
from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings  # ← ADD THIS LINE
from django.conf.urls.static import static  # ← ADD THIS LINE


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage_view, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('menu/', include('menus.urls')),
    path('reservations/', include('reservations.urls')),
    path('categories/', include('categories.urls')),
]


# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])