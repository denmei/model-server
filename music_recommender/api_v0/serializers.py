from rest_framework import serializers
from music_recommender.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    """
    List of artists available.
    """

    class Meta:
        model = Artist
        fields = '__all__'

