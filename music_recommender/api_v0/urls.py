from django.conf.urls import url
from music_recommender.api_v0.views import get_recommendation, ArtistList
from music_recommender.ml_model.recommender import get_model_data

urlpatterns = [
    url(r'^artist_list$',ArtistList.as_view(), name='artist_list_api'),
    url(r'^artist_recommendation$', get_recommendation, name='artist_recommendation_api'),
]
"""
url(r'^artist_list$', ArtistList.as_view(), name='artist_list_api'),
    url(r'^artist_recommendation/(?P<artist>.*)/(?P<number>\d+)$', get_recommendation, name='artist_recommendation_api'),
"""

get_model_data()  # cache data and model when app is starting to increase prediction speed
