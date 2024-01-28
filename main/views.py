from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def main(request):

   card=models.Card.objects.all() 
   cardproduct=models.CardProduct.objects.all() 
   category=models.Category.objects.all() 
   product=models.Product.objects.all() 
   productimage=models.ProductImage.objects.all() 
   productreview=models.ProductReview.objects.all() 
   wishList=models.WishList.objects.all() 

   context={
      'card':card,
      'cardproduct':cardproduct,
      'category':category,
      'product':product,
      'productimage':productimage,
      'productreview':productreview,
      'wishList':wishList
   }
   
   return render(request, 'index.html', context)


from django.shortcuts import render
from .models import Card, CardProduct, Category, Product, ProductImage, ProductReview, WishList

def cards(request):
    cards = Card.objects.all()
    return render(request, 'index.html', {'cards': cards})


def card_product(request):
    card_products = CardProduct.objects.all()
    return render(request, 'index.html', {'card_products': card_products})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_image(request):
    product_images = ProductImage.objects.all()
    return render(request, 'index.html', {'product_images': product_images})


def product_review(request):
    product_reviews = ProductReview.objects.all()
    return render(request, 'index.html', {'product_reviews': product_reviews})


def wishlist(request):
    wishlists = WishList.objects.all()
    return render(request, 'index.html', {'wishlists': wishlists})



def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
       
            user = User.objects.create_user(username=username, password=password)


            return redirect('index.html')

        except Exception as e:
            
            return render(request, 'login.html', {'error_message': str(e)})

   
    return render(request, 'login.html')








