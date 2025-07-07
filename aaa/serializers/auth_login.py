from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        if not phone or not password:
            raise serializers.ValidationError("Phone and password are required.")

        user = authenticate(phone=phone, password=password)

        if not user:
            raise serializers.ValidationError("Invalid phone or password.")

        attrs['user'] = user
        return attrs
