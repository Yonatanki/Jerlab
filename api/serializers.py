from rest_framework import serializers
from devices.models import ADC, Router

class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = '__all__'

class ADCSerializer(serializers.ModelSerializer):
    Router_Management = RouterSerializer(many=False)

    class Meta:
        model = ADC
        fields = '__all__'

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

# class alteonGetRequest(serializers.Serializer):
    # d = serializers.restGetRequest()