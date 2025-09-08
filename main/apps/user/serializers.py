from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):   
    confirm_password = serializers.CharField(
        write_only = True,
        required = True,
        help_text = 'Enter confirm password',
        style = {'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "role",
            'password',
            'confirm_password'
        )    

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('confirm_password'):
            raise serializers.ValidationError({"message":"Password and confirm password don't match"}) 
        validated_data.pop('confirm_password') 
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['id'] = self.user.id
        data['guid'] = self.user.guid
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['role'] = self.user.role
        return data
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

