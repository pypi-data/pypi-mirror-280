from django.core import exceptions
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from phonenumber_field import serializerfields
from users.models import User,ResetPasword
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from google.oauth2 import id_token
from google.auth.transport import requests

from rest_registration.api.serializers import DefaultUserProfileSerializer



class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password])
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {'password': {'write_only':True}},
        }

    def create(self, validated_data):
        
        user = User.objects.create(**validated_data)
        
        user.set_password(validated_data['password'])
        user.save()

        return user   



class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        fields = ['password','password_confirm']
   
    def validate(self, data):
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        errors = dict()

        if password != password_confirm:
            errors['password_confirm'] = ['Passwords do not match.']

        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(ResetPasswordSerializer, self).validate(data)



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'image',
            'get_full_name',
            'my_purchases_count',
            'my_reviews_count',
            'my_products_count',
            'my_orders_count',
            'mbank_number'
            )

    def update(self, instance, validated_data):
        image = validated_data.get('image', instance.image)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mbank_number = validated_data.get('mbank_number', instance.mbank_number)

        if image is None and validated_data['image'] is None or not 'image' in validated_data:
            instance.save()
        
        else:
           instance.image=image 
           instance.save()

        return instance 



class GoogleAuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()

    def create(self, validated_data):
        try:
            tooken = id_token.verify_oauth2_token(
                validated_data['token'], requests.Request(), settings.GOOGLE_OAUTH2_CLIENT_ID
            )
        except Exception as e:
            raise ValueError('Bad token Google')
        print("data USER",tooken,"\n")
        user, _ = User.objects.get_or_create(email=tooken.get('email',validated_data['email']),auth_provider=User.AUTH_PROVIDERS.get('google'))
        user.first_name=tooken.get('given_name',None)
        user.last_name = tooken.get('family_name',None)
        user.full_name = tooken.get('name',None)
        user.last_name=tooken.get('family_name',None)
        user.image_url=tooken.get('picture',None)
        user.save()
    
        return user