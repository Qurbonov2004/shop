from django.urls import path
from dashboard.views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('category/list/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/update/<int:id>/', category_update, name='category_update'),
    path('category/delete/<int:id>/', category_delete, name='category_delete'),
    path('product/list/', product, name='product'),
    path('product/create/', product_create, name='product_create'),
    path('product/delete/<int:id>/', product_delete, name='product_delete'),
    path('product/update/<int:id>/', product_update, name='product_update'),
    path('enter/create/', create_enter, name='create_enter'),
    path('enter/update/<int:id>/', update_enter, name='update_enter'),
    path('create/delete/<int:id>/', delete_enter, name='delete_enter'),
    path('enter/list/', list_enter, name='list_enter'),
    path('product/write/', write, name='write'),
    path('product/enter_write/', enter_write, name='enter_write'),
    path('product/expenditure/', expenditure, name='expenditure'),
    path('product/expenditure_excel/', expenditure_excel, name='expenditure_excel'),
    path('product/upload_excel/', upload_excel, name='upload_excel'),
    path('product/list_enter/', list_enter, name='list_enter'),
]

