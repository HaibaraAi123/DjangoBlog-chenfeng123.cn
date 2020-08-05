#coding=utf-8
from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('detail/<int:id>/', views.ArticleDetail, name='detail'),

]
