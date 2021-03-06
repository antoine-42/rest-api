from rest_framework import serializers

from game_api.models import Game, Studio, Platform


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ["id", "name"]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["id", "name"]


class GameSerializer(serializers.ModelSerializer):
    studio = serializers.SlugRelatedField(
        queryset=Studio.objects.all(), slug_field="name"
    )
    platforms = serializers.SlugRelatedField(
        queryset=Platform.objects.all(), many=True, slug_field="name"
    )

    class Meta:
        model = Game
        fields = ["id", "name", "release_date", "studio", "ratings", "platforms"]
