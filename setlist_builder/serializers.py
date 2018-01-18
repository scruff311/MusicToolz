from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'title', 'tuning', 'starting_note', 'ending_note',
                  'starting_fifth', 'actual_tuning', 'active')
