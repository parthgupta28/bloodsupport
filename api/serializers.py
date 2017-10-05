from rest_framework import serializers
from .models import bloodbank



class bloodbankSerializer(serializers.ModelSerializer):
    class Meta :
        model = bloodbank
        fields = '__all__'