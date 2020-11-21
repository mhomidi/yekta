from rest_framework import serializers

from models.URL.models import URL


class URLSerializer(serializers.ModelSerializer):

    class Meta:
        model = URL
        fields = ('address', )