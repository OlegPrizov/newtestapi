from rest_framework import serializers

from advertisment.models import Advertisement

class AdvertismentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'