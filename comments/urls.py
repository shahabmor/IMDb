from django.urls import path
from .views import *
app_name = 'comment'

urlpatterns = [
    path('<int:pk>', add_comment, name='add-comment'),
    path('reply/<int:pk>', movie_comments, name='movie-comments'),
    path('delete/<int:pk>', comment_delete, name='comment_delete'),
    path('edit/<int:pk>', edit_comment, name='edit_comment')
]
