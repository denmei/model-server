from rest_framework import serializers
from music_recommender.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    """
    List of artists available.
    """

    class Meta:
        model = Artist
        fields = '__all__'

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        ret['name'] = ret['name'].title()
        return ret

