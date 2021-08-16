from rest_framework import serializers

from game_api.models import Game, Studio, Platform


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ["name"]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["name"]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["name", "release_date", "studio", "ratings", "platforms"]
