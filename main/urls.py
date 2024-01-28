from django.urls import path
from .views import main,login
urlpatterns=[
    path('',main, name='main'),
    path('main/register/', login , name='register'),
]