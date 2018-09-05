from django.conf.urls import url
from music_recommender.api_v0.views import get_recommendation

urlpatterns = [
    url(r'^artist-recommendation$', get_recommendation, name='artist-recommendation-api'),
]