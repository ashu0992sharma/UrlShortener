from rest_framework import serializers

from . import models, utils

from rest_framework_mongoengine import serializers as MongoSerializer


class UrlShortenerCreateSerializer(MongoSerializer.DocumentSerializer):
    """serializer for UrlShortener Serializer"""
    url = serializers.URLField()
    hash = serializers.CharField(required=False)
    
    class Meta:
        model = models.UrlHashMapping
        exclude = ("id",)
        
    def create(self, validated_data):
        """creating hash for url"""
        hash = utils.gen_hash()
        validated_data["hash"] = hash
        instance = False
        while not instance:  # retrying if getting duplicate hash 
            try:
                # instance = models.UrlHashMapping.objects.create(**validated_data)
                instance = self.recursive_save(validated_data) 
            except:
                continue
        return instance
            

class UrlShortenerGetHashSerializer(MongoSerializer.DocumentSerializer):
    """serializer for UrlShortener Serializer"""

    class Meta:
        model = models.UrlHashMapping
        fields = ("hash",)
        
        
class UrlShortenerGetUrlSerializer(MongoSerializer.DocumentSerializer):
    """serializer for UrlShortener Serializer"""

    class Meta:
        model = models.UrlHashMapping
        fields = ("url",)
        
        
class UrlShortenerValidateUrlSerializer(serializers.Serializer):
    """serializer for UrlShortener Serializer"""
    hash = serializers.CharField(max_length=8)
    
    def validate_hash(cself, hash):
        """validating hash"""
        if not utils.validate_hash(hash):
            raise serializers.ValidationError("Invalid hash")
        return hash
        
    
