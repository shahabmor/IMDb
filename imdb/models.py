from django.db import models

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