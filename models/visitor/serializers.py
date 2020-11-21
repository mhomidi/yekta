from rest_framework import serializers

from models.visitor.models import Visitor


class VisitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visitor
        fields = ('url', 'device', 'browser', 'date', 'ip')
