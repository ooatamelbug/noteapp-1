from rest_framework import serializers
from .models import Note
from django.contrib.auth.admin import User
from rest_framework.authtoken.views import Token

'''
class NoteSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    alarm = serializers.DateTimeField()
    type = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.alarm = validated_data.get('alarm', instance.alarm)
        instance.type = validated_data.get('type', instance.type)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance
    class Meta:
        model = Note
        fields = '__all__'
'''


class NoteListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'user', 'body', 'created_at', 'alarm', 'type')


class NoteRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'body', 'created_at', 'alarm', 'type')


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        Token.objects.create(user=user_obj)
        return validated_data
