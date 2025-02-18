from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        email_exists = User.objects.filter(email=self.validated_data['email']).exists()
        passwords_dont_matching = bool(pw != repeated_pw)

        if passwords_dont_matching:
            raise serializers.ValidationError({'error': 'password dont match'})
    
        if email_exists: 
            raise serializers.ValidationError({'error': 'email adress already exists'})
        account = User(email = self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account
            
