from django.urls import path
from .views import *
urlpatterns=[
    path('',main, name='main'),
    path('main/register/', login , name='account'),
    path('dashboard/',adminka, name='dashboard'),
    path('category/list',category_list,name='category_list'),
    path('category/create/',category_create,name='category_create'),
    path('category/update/<int:id>/',category_update,name='category_update'),
    path('category/delete/<int:id>/',category_delete,name='category_delete'),
    path('product/list',product,name='product'),
    path('product/create',product_create,name='product_create'),
    path('product/delete/<int:id>/',product_delete,name='product_delete'),
    path('product/update/<int:id>/',product_update,name='product_update'),
]