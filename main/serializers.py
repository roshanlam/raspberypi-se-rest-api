from rest_framework import serializers

from .models import website

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = website
        fields = '__all__'