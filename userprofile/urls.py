from django.urls import path
from . import views


app_name = 'userprofile'
urlpatterns = [
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('register/', views.UserRegister, name='register'),
    path('edit/<int:id>/', views.UserProfileEdit, name='edit')
]