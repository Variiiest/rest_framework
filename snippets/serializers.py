from rest_framework import serializers
from .models import Snippet 

class SnippetSerializer(serializers.Serializer):
    title= serializers.CharField(max_length= 100)
    code = serializers.CharField()
    language = serializers.CharField(max_length= 100)
    
    
    
    def create(self, validated_data):
        """
        Create and return a new Snippet instance , given the validated_data.
        """
        return Snippet.objects.create(**validated_data)
    
    
    def update(self,instance, validated_data):
        instance.title= validated_data.get('title', instance.title)
        instance.code= validated_data.get('code', instance.code)
        instance.language= validated_data.get('language', instance.language)
        instance.save()
        return instance
    
    


