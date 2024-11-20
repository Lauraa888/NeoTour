from rest_framework import serializers
from .models import Tour, Review, Application

class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'tour', 'name', 'email', 'message']  
        
class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'tour', 'name', 'email', 'message']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'tour', 'username', 'user_image', 'comment']

class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'title', 'category', 'location']

class TourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['title', 'category', 'location', 'description']

class TourDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Вложенный сериализатор для отзывов

    class Meta:
        model = Tour
        fields = ['title', 'category', 'location', 'description', 'reviews']


