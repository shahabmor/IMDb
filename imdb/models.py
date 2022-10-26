from django.db import models
import pillow

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Role(models.Model):
    title = models.CharField(max_length=50)


class Crew(models.Model):
    MALE = 1
    FEMALE = 0
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.PositiveSmallIntegerField(null=True, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True)
    avatar = models.ImageField(upload_to='actors/', null=True, blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='movies/', null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    crew = models.ManyToManyField(Crew)

class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    join_date = models.DateField(null=True)