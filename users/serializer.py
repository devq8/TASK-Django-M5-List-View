from dataclasses import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserCreateSerializer(serializers.ModelSerializer):
    #this code to hide the password in response
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    #adjust create method for serializer, so when a User object is created, the password value will be hashed.
    def create(self, validate_date):
        username = validate_date["username"]
        password = validate_date["password"]
        first_name = validate_date["first_name"]
        last_name = validate_date["last_name"]
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return new_user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    access = serializers.CharField(allow_blank= True, read_only= True)

    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")

        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist!")
        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect password!")

        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)

        data["access"] = token
        
        return data