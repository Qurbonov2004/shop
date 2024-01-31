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
   
   return render(request, 'asosiy/index.html', context)


from django.shortcuts import render
from .models import Card, CardProduct, Category, Product, ProductImage, ProductReview, WishList

def cards(request):
    cards = Card.objects.all()
    return render(request, 'asosiy/index.html', {'cards': cards})


def card_product(request):
    card_products = CardProduct.objects.all()
    return render(request, 'asosiy/index.html', {'card_products': card_products})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'asosiy/index.html', {'categories': categories})


def products(request):
    products = Product.objects.all()
    return render(request, 'asosiy/index.html', {'products': products})


def product_image(request):
    product_images = ProductImage.objects.all()
    return render(request, 'asosiy/index.html', {'product_images': product_images})


def product_review(request):
    product_reviews = ProductReview.objects.all()
    return render(request, 'asosiy/.html', {'product_reviews': product_reviews})


def wishlist(request):
    wishlists = WishList.objects.all()
    return render(request, 'asosiy/.html', {'wishlists': wishlists})



def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:
       
            user = User.objects.create_user(username=username, password=password)


            return redirect('asosiy/index.html')

        except Exception as e:
            
            return render(request, 'asosiy/account.html', {'error_message': str(e)})

   
    return render(request, 'asosiy/account.html')







#dashboard



def adminka(request):
    category=models.Category.objects.all()
    product=models.Product.objects.all()

    context={
        'category':category,
        'product':product
    }

    return render(request,'dashboard/index.html',context)


def category_list(request):
    categoriess=models.Category.objects.all()
    return render(request,'dashboard/category/list.html',{'categoriess':categoriess})


def category_create(request):
    if request.method=='POST':
        models.Category.objects.create(
            name=request.POST['name']
        )
        return redirect('category_list')
    return render(request,'dashboard/category/create.html')


def category_update(request,id):
    category=models.Category.objects.get(id=id)
    if request.method=='POST':
        category.name = request.POST['name']
        category.save()
        return redirect('category_list')
    return render(request,'dashboard/category/update.html',{'category':category})



def category_delete(request,id):
    category=models.Category.objects.get(id=id)
    category.delete()

    return redirect('category_list')







def product(request):
    products=models.Product.objects.all()

    return render(request,'dashboard/product/list.html',{'products':products})


def product_create(request):
    if request.method=='POST':
        
        name=request.POST['name'],
        description=request.POST['description'],
        quantity=request.POST['quantity'],
        price=request.POST['price'],
        currency=request.POST['currency'],
        discount_price=request.POST['discount_price'],
        baner_image= request.FILES['image'],
        category = models.Category.objects.get(id=request.POST['category_id'])
        models.Product.objects.create(
            name=name,
            description=description,
            quantity=quantity,
            price=price,
            currency=currency,
            discount_price=discount_price,
            baner_image=baner_image,
            category=category
        )
        return redirect('product')
        
    return render(request,'dashboard/product/create.html',{'category':models.Category.objects.all()})


def product_update(request,id):
    product=models.Product.objects.get(id=id)
    if request.method=='POST':
        product.name=request.POST['name']
        product.description=request.POST['description']
        product.quantity=request.POST['quantity']
        product.currency=request.POST['currency']
        product.discount_price=request.POST['discount_price']
        product.baner_image=request.POST['baner_image']
        product.category=request.POST['category']

        product.save()

        return redirect('product')
    category=models.Category.objects.all()

    context={
        'product':product,
        'category':category

    }
    
    return render(request,'dashboard/product/update.html',context)







def product_delete(request,id):
    product=models.Product.objects.get(id=id)
    product.delete()

    return redirect('product')