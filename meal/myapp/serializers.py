from rest_framework import serializers
from .models import meals
class mealSerializer(serializers.ModelSerializer):
    class Meta:
        model = meals
        fields = '__all__'
