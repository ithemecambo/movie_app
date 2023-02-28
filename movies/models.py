from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, blank=True, null=True, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return f'{self.text}'


