from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from user.models import User

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token['email'] = user.email

        return token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):

        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            telephone=validated_data['telephone'],
            cpf=validated_data['cpf'],
            rg=validated_data['rg']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user