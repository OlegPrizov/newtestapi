from rest_framework import viewsets, mixins

from advertisment.models import Advertisement
from .serializers import AdvertismentSerializer

class AdvertisementViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = AdvertismentSerializer
    queryset = Advertisement.objects.all()
