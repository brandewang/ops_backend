from rest_framework import serializers
from api.models import AppGrp, App, User


class AppGrpSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGrp
        fields = '__all__'


class AppSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField()
    class Meta:
        model = App
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
