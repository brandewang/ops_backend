from rest_framework import serializers
from api.models import AppGrp, App, User

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'