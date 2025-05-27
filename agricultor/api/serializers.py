from rest_framework import serializers
from agricultor import models

class AgricultorSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Agricultor
        fields = '__all__'