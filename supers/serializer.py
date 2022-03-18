from rest_framework import serializers

import supers
from .models import Supers

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'second_ability', 'catchphrase', 'super_type_id']