from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.name}"
    
    # def save(self, *args, **kwargs):
    #     if self.name == "Yoko Ono's blog":
    #         return  # Yoko shall never have her own blog!
    #     else:
    #         super().save(*args, **kwargs)
    
class Director(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to = 'images/directors/', null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Movie(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    story = models.CharField(max_length=2048, null=True, blank=True)
    trailer = models.URLField(max_length=200, null=True, blank=True)
    director = models.ForeignKey(Director,on_delete= models.CASCADE, related_name="movies")
    genres = models.ManyToManyField(Genre, blank=True, related_name="movies")
    poster = models.ImageField(upload_to = 'images/movies/', null=True)
    
    def __str__(self):
        return f"{self.name}"
