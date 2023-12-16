#serializers are classes that take a certain model that we want to serialize or object and will turn it into JSON data 

from rest_framework.serializers import ModelSerializer
from base.models import Room

class SerializeRoom(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'