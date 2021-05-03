from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.db import router
from rest_framework import routers
from movies.views import MovieViewSet


router =  routers.DefaultRouter()
router.register('movies', MovieViewSet) # prefix = movies, viewset = MovieViewSet

# router는 이를 바탕으로 url 매핑
'''
    URL pattern : ^moviews/$ Name: 'movie-list'
    URL pattern : ^moviews/{PK}/$ Name: 'movie-detail'
'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
