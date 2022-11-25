from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.

# Abstract Comment
class AbstractComment(models.Model):

    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40
    status_choices = (
        (CREATED, 'created'),
        (APPROVED, 'approved'),
        (REJECTED, 'rejected'),
        (DELETED, 'deleted')
    )

    parent = models.ForeignKey('self', on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)ss')
    comment_body = models.TextField(blank=True, null=True)

    status = models.PositiveSmallIntegerField(choices=status_choices, default=CREATED)
    validated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='validated_%(class)ss'
    )

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Movie Comment
class MovieComment(AbstractComment):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='%(class)ss')

