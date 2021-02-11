from rest_framework import serializers
from .models import Snippet 
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= Snippet
        fields= '__all__'
    # title= serializers.CharField(max_length= 100)
    # code = serializers.CharField()
    # language = serializers.CharField(max_length= 100)
    
    
    
    # def create(self, validated_data):
    #     """
    #     Create and return a new Snippet instance , given the validated_data.
    #     """
    #     return Snippet.objects.create(**validated_data)
    
    
    # def update(self,instance, validated_data):
    #     instance.title= validated_data.get('title', instance.title)
    #     instance.code= validated_data.get('code', instance.code)
    #     instance.language= validated_data.get('language', instance.language)
    #     instance.save()
    #     return instance
    
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= User 
        fields= ['id', 'username']
    
    


