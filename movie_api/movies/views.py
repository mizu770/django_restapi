from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie


# viewset 사용 시 CRUD 로직을 직접 코딩 하지 않고 기능을 사용 가능

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

