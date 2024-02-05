from django.urls import path
from .views import *
urlpatterns=[
    path('',main, name='main'),
    path('cards/',cards, name='cards'),
    path('detail/<int:id>',detail, name='detail'),
    path('main/register/', login , name='account'),
    #dashboard
    path('dashboard/',dashboard, name='dashboard'),
    path('category/list',category_list,name='category_list'),
    path('category/create/',category_create,name='category_create'),
    path('category/update/<int:id>/',category_update,name='category_update'),
    path('category/delete/<int:id>/',category_delete,name='category_delete'),
    path('product/list',product,name='product'),
    path('product/create',product_create,name='product_create'),
    path('product/delete/<int:id>/',product_delete,name='product_delete'),
    path('product/update/<int:id>/',product_update,name='product_update'),
    path('carts',carts,name='carts'),
    path('cart_detail/<int:id>',cart_detail,name='cart_detail'),
    path('cart_detail_delete/<int:id>',cart_detail_delete,name='cart_detail_delete'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('register', register, name='register'),
    path('edit', edit, name='edit'),
]