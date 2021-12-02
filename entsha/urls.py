from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('delphius/', include('delphius.urls')),
    path('intelliview/', include('intelliview.urls')),
    path('NGBS/', include('NGBS.urls')),
    path('NGMC/', include('NGMC.urls')),
    path('del_connect/', include('del_connect.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
