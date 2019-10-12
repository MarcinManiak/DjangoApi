from rest_framework import serializers
from .models import Dates

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dates
        fields = ['id','topic','type', 'descr', 'author', 'date', 'updated_at']