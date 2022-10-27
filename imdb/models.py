from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)


class Role(models.Model):
    title = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)


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
    avatar = models.ImageField(upload_to='crew/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='movies/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)
    genres = models.ManyToManyField(Genre)
    crew = models.ManyToManyField(Crew, through='MovieCrew')


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('movie', 'crew', 'role')