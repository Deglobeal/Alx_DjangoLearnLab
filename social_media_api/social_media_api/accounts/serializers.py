from rest_framework import serializers
from . models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        feilds = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True},
            'profile_picture': {'required': False},
            'bio': {'required': False, 'allow_blank': True},
        }
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        return user
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')
        read_only_fields = ('id', 'username', 'followers', 'following')
        
