from rest_framework import serializers 
from tutorials.models import Monuments
from tutorials.models import LocalFood
 

        
class MonumentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Monuments
        fields = ('id',
                  'title',
                  'description',
                  'history')
        
class LocalFoodSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = LocalFood
        fields = ('id',
                  'title',
                  'description',
                  'history')