from rest_framework.generics import ListCreateAPIView

from game_api.models import Game, Studio, Platform
from game_api.serializers import GameSerializer, StudioSerializer, PlatformSerializer


class StudioListCreateView(ListCreateAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class PlatformListCreateView(ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class GameListCreateView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
