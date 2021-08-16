from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"


class Platform(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"


class Game(models.Model):
    name = models.CharField(max_length=150, unique=True)
    release_date = models.DateField()
    studio = models.ForeignKey(Studio, related_name="games", on_delete=models.SET_NULL, null=True)
    ratings = models.IntegerField()
    platforms = models.ManyToManyField(Platform, related_name="games")
