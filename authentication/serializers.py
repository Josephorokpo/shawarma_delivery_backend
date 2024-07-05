from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField



class HelloAuthSerializer(serializers.Serializer):
    message = serializers.CharField()

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=60)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail='Username already exists')

        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail='User with this email already exists')

        phonenumber_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()
        if phonenumber_exists:
            raise serializers.ValidationError(detail='User with this phone number already exists')

        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
