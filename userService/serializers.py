from rest_framework import serializers
from .models import SysUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = '__all__'

