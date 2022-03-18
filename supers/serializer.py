from rest_framework import serializers
from .models import Supers

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'second_ability', 'catchphrase', 'super_type_id']
        depth = 1
    
    super_type_id = serializers.IntegerField(write_only=True)
    