from django.db.models import fields
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie # 모델 설정
        fields = ('id', 'title', 'genre', 'year') # 사용 할 필드 설정
        