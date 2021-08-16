from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

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
    serializer_class = GameSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Game.objects.all()

        year = self.request.query_params.get('year')
        if year is not None:
            queryset = queryset.filter(release_date__year=year)

        date = self.request.query_params.get('date')
        if date is not None:
            queryset = queryset.filter(release_date=date)

        studio = self.request.query_params.get('studio')
        if studio is not None:
            queryset = queryset.filter(studio__name=studio)

        platform = self.request.query_params.get('platform')
        if platform is not None:
            queryset = queryset.filter(platforms__name=platform)

        ratings_above = self.request.query_params.get('ratings.above')
        if ratings_above is not None:
            queryset = queryset.filter(ratings__gt=ratings_above)

        ratings_below = self.request.query_params.get('ratings.below')
        if ratings_below is not None:
            queryset = queryset.filter(ratings__lt=ratings_below)

        return queryset


class GameRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "id"
