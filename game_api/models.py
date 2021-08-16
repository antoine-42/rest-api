from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Platform(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Game(models.Model):
    name = models.CharField(max_length=150, unique=True)
    release_date = models.DateField()
    studio = models.ForeignKey(Studio, related_name="games", on_delete=models.SET_NULL, null=True)
    ratings = models.IntegerField()
    platforms = models.ManyToManyField(Platform, related_name="games")
