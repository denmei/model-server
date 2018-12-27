# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from music_recommender.ml_model.recommender import get_artist_recommendations
from rest_framework import generics
from music_recommender.models import Artist
from music_recommender.api_v0.serializers import ArtistSerializer


@api_view(['POST'])
def get_recommendation(request):
    data = request.data
    artist = data['artist']
    number = int(data['number'])
    response = dict(recommendations=get_artist_recommendations(artist, number))
    return Response(response)


"""
@api_view(['GET'])
def get_recommendation(request, artist, number):
    print(unicodedata.normalize('NFD', artist).encode('utf-8', 'ignore'))
    artist = str(unquote(artist))
    number = int(number)
    print(number)
    print(artist)
    response = dict(recommendations=get_artist_recommendations(artist, number))
    print(response)
    return Response(response)
"""


class ArtistList(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        return Artist.objects.all()
