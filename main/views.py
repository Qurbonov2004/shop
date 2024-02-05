from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import Card, CardProduct, Category, Product, ProductImage, ProductReview, WishList


def main(request):

   card=Card.objects.all() 
   cardproduct=CardProduct.objects.all() 
   category=Category.objects.all() 
   product=Product.objects.all() 
   productimage=ProductImage.objects.all() 
   productreview=ProductReview.objects.all() 
   wishList=WishList.objects.all()
   productreview=ProductReview.objects.all()

   context={
      'card':card,
      'cardproduct':cardproduct,
      'category':category,
      'product':product,
      'productimage':productimage,
      'productreview':productreview,
      'wishList':wishList,
      'productreview':productreview ,
      'user': request.user
        
      
   }
   
   return render(request, 'asosiy/index.html', context)




def cards(request):
    cards = Card.objects.all()
    return render(request, 'asosiy/index.html', {'cards': cards, 'user':request.user})


def card_product(request):
    card_products = CardProduct.objects.all()
    return render(request, 'asosiy/index.html', {'card_products': card_products})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'asosiy/index.html', {'categories': categories})


def products(request):
    products = Product.objects.all()
    return render(request, 'asosiy/index.html', {'products': products})




#vazivaga


def detail(request, id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=id)
    images = ProductImage.objects.all()
    category_id = product.category.id if product.category else None
    
    recomendation = Product.objects.filter(category_id=category_id).exclude(id=product.id)[:3]

    context = {
        'products': products,
        'product': product,
        'images': images,
        'range': range(int(product.review)),
        'recomendation': recomendation
    }

    return render(request, 'asosiy/single.html', context)







def product_image(request):
    product_images = ProductImage.objects.all()
    return render(request, 'asosiy/index.html', {'product_images': product_images})


def product_review(request):
    product_reviews = ProductReview.objects.all()
    return render(request, 'asosiy/.html', {'product_reviews': product_reviews})


def wishlist(request):
    wishlists = WishList.objects.all()
    return render(request, 'asosiy/.html', {'wishlists': wishlists})





from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            return redirect('main')
        else:
            return render(request, 'asosiy/account.html', {'error_message': 'Invalid email or password'})

    return render(request, 'asosiy/login/account.html')













def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password == password_confirmation:
            user = User.objects.create_user(username=username, password=password)
            return redirect('main')
        else:
            return render(request, 'asosiy/login/register.html', {'error_message': 'Passwords do not match'})
    
    return render(request, 'asosiy/login/register.html')



    





@login_required
def edit(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        user = request.user
        if password == password_confirmation:
            user.username = username
            user.set_password(password)
            user.save()
            return redirect('register')  
        

    return render(request, 'asosiy/login/edit.html',{'user':request.user})

#dashboard



def dashboard(request):
    category=Category.objects.all()
    product=Product.objects.all()

    context={
        'category':category,
        'product':product
    }

    return render(request,'dashboard/index.html',context)


def category_list(request):
    categoriess=Category.objects.all()
    return render(request,'dashboard/category/list.html',{'categoriess':categoriess})


def category_create(request):
    if request.method=='POST':
        Category.objects.create(
            name=request.POST['name']
        )
        return redirect('category_list')
    return render(request,'dashboard/category/create.html')


def category_update(request,id):
    category=Category.objects.get(id=id)
    if request.method=='POST':
        category.name = request.POST['name']
        category.save()
        return redirect('category_list')
    return render(request,'dashboard/category/update.html',{'category':category})



def category_delete(request,id):
    category=Category.objects.get(id=id)
    category.delete()

    return redirect('category_list')







def product(request):
    products=Product.objects.all()

    return render(request,'dashboard/product/list.html',{'products':products})


def product_create(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        quantity = request.POST['quantity']
        price = request.POST['price']
        currency = request.POST['currency']
        baner_image = request.FILES['image']
        category_id = request.POST['category_id']
        images = request.FILES.getlist('images')
        product = Product.objects.create(
            name=name,
            description = description,
            quantity=quantity,
            price=price,
            currency=currency,
            baner_image=baner_image,
            category_id=category_id
        )
        for image in images:
            ProductImage.objects.create(
                image=image,
                product=product
            )
            print(images)
    return render(request, 'dashboard/product/create.html', context)


def product_update(request, id):
    product = Product.objects.get(id=id)
    
    # Eski rasmi saqlab qolish
    old_banner_image = product.baner_image
    
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        
        # Quantity maydoni uchun qiymatni tekshirib chiqish
        quantity = request.POST.get('quantity', '')
        product.quantity = int(quantity) if quantity.isdigit() and quantity != '' else 0

        product.currency = request.POST['currency']
        product.discount_price = request.POST['discount_price']
        new_images = request.FILES.getlist('images')
        for new_image in new_images:
            ProductImage.objects.create(
                image=new_image,
                product=product
            )
        old_images = ProductImage.objects.filter(product=product)
        for old_image in old_images:
            old_image.delete()
        if 'image' in request.FILES:
            product.baner_image = request.FILES['image']
        else:
            product.baner_image = old_banner_image

        product.category_id = request.POST['category_id']
        
        product.save()

        return redirect('product')
    
    category = Category.objects.all()

    context = {
        'product': product,
        'category': category
    }

    return render(request, 'dashboard/product/update.html', context)


def product_delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()

    return redirect('product')


def carts(request):
    active=Card.objects.filter(is_active=True,user=request.user)
    in_active=Card.objects.filter(is_active=False,user=request.user)
    context={
        'active':active,
        'in_active':in_active
    }
    return render(request,'asosiy/carts.html',context)


def cart_detail(request,id):
    cart=Card.objects.get(id=id)
    items=CardProduct.objects.filter(card=cart)

    context={
        'cart':cart,
        'items':items
    }
    return render(request,'asosiy/cart_detail.html',context)


def cart_detail_delete(request):
    item_id = request.GET['items_id']
    item = CardProduct.objects.get(id=item_id)
    cart_id = item.card.id
    item.delete()
    return redirect('main:cart_detail', cart_id)




from django.shortcuts import get_object_or_404

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    user = request.user
    active_card = Card.objects.filter(user=user, is_active=True).first()

    if not active_card:
        active_card = Card.objects.create(user=user)


    existing_product = CardProduct.objects.filter(card=active_card, product=product).first()

    if existing_product:
        existing_product.quantity += 1
        existing_product.save()
    else:
        CardProduct.objects.create(card=active_card, product=product, quantity=1)
    return redirect('carts')







