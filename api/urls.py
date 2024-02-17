from django.urls import path
from . import views

urlpatterns=[
    path('product/',views.listproduct),
    path('category/',views.listcategory),
    path('review/',views.listreview),
    path('product/images/',views.listproductimage),
    path('card/',views.listcard),
    path('cardproduct/',views.listcardproduct),
    path('enterproduct/',views.listenterproduct),
    path('wishlist/',views.listwishlist)
]