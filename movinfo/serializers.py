from django.contrib.auth.models import User, Group
from rest_framework import serializers,
from rest_framework import Movies
from .models import Movies

"""
After setting up REST Framework, we need to specify how our data will be Serialized. 
Final output data has to be serialized into a specific format, and nput data will be
de-serialized for processing.
Serializers: provides serialization for normal python class instances.
ModelSerializers: It provides serialization for model instances.
Meta class allows you to specify the model to serialize and the fields to be included for serialization. All model 
fields will be included if you don't set a fields attribute.
"""

class MoviesListSeralizer(serializers.ModelSerializer):

    class Meta:
        model = Movies

        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
