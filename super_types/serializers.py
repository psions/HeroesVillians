from rest_framework import serializers
from .super import SuperTypes

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = SuperTypes
        type = ['hero','villain']
        depth = 1
    
super_type_id = serializers.IntegerField(write_only=True)