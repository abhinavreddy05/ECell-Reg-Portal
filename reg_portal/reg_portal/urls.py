from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('landingPage.urls'), name="home"),
    path('ead/', include('ead.urls'), name="ead"),
    path('lsm/', include('lsm.urls'), name="lsm"),
    path('empresario/', include('empresario.urls'), name="empresario"),
]
