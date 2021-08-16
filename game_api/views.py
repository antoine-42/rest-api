from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from game_api.models import Game, Studio, Platform
from game_api.serializers import GameSerializer, StudioSerializer, PlatformSerializer


class StudioListCreateView(ListCreateAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class StudioRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    lookup_field = "id"


class PlatformListCreateView(ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    lookup_field = "id"


class GameListCreateView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "id"
