from rest_framework import serializers
from iotapp.models import don

# Serializers define the API representation.
class Dhser(serializers.ModelSerializer):
    class Meta:
        model = don
        fields = '__all__'
