from django.db import models
from django.utils import timezone
# from likert_field.models import LikertField

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre)
    cover_image_url = models.CharField(max_length=500, blank=True)
    # track_rating = LikertField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
