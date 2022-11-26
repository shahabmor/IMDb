from django.urls import path
from .views import add_comment,movie_comments

app_name = 'comment'

urlpatterns = [
    path('<int:pk>', add_comment, name='add-comment'),
    path('reply/<int:pk>', movie_comments, name='movie-comments')
]
