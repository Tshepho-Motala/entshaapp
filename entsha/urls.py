from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('delphius/', include('delphius.urls')),
    path('intelliview/', include('intelliview.urls')),
    path('NGBS/', include('NGBS.urls')),
    path('NGMC/', include('NGMC.urls')),
    path('del_connect/', include('del_connect.urls')),
    
]
