from django.urls import path
from . import views


app_name = 'comment'
urlpatterns = [
    path('<int:article_id>', views.post_comment, name='post_comment'),
    path('<int:article_id>/<int:parent_comment_id', views.post_comment, name='reply_comment'),
]
