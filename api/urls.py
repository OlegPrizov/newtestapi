from django.urls import include, path
from rest_framework import routers

from .views import AdvertisementViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'ads', AdvertisementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]