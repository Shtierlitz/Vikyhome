# api/cleaning/serializers.py

from rest_framework.serializers import ModelSerializer

from .models import Service, Extra, Post


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "title", "description", 'price', "price_description", 'image')


class ExtraSerializer(ModelSerializer):
    class Meta:
        model = Extra
        fields = ("id", "title", "price", "price_description")


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "text")

