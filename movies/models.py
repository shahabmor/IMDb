from django.db import models


# Create your models here.

class ValidManager(models.Manager):
    def get_queryset(self):
        return super(ValidManager, self).get_queryset().filter(is_valid=True)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=50, null=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Crew(models.Model):
    MALE = 1
    FEMALE = 0
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    gender = models.PositiveSmallIntegerField(null=True, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='crew/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    imdb_score = models.FloatField(blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='movies/avatars/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)
    genres = models.ManyToManyField(Genre)
    crew = models.ManyToManyField(Crew, through='MovieCrew', related_name='movies')

    objects = models.Manager()
    valid = ValidManager()

    def __str__(self):
        return self.title


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True, null=True)
    modified_time = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('movie', 'crew', 'role')
