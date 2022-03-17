from rest_framework import serializers
from .models import super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'second_ability', 'catchphrase', 'super_type_id']