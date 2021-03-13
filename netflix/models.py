from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True )
    overview = models.TextField(null=True, blank=True)
    year = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='movies/posters', null=True, blank=True)
    video = models.FileField(upload_to='movies/videos', null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        # Add str to avoid errors
        return str(self.name)
