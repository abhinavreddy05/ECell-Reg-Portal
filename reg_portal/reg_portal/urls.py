from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('landingPage.urls'), name="home"),
    path('ead/', include('ead.urls'), name="ead"),
    path('lsm/', include('lsm.urls'), name="lsm"),
    path('empresario/', include('empresario.urls'), name="empresario"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)