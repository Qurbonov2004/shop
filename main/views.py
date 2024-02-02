from django.shortcuts import render,redirect


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Card, CardProduct, Category, Product, ProductImage, ProductReview, WishList


def main(request):

   card=Card.objects.all() 
   cardproduct=CardProduct.objects.all() 
   category=Category.objects.all() 
   product=Product.objects.all() 
   productimage=ProductImage.objects.all() 
   productreview=ProductReview.objects.all() 
   wishList=WishList.objects.all() 

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




#vazivaga

def detail(request,id  ):
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    images=ProductImage.objects.all()
    context={
        'products':products,
        'product':product,
        'images':images

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
    if request.method=='POST':
        
        name=request.POST['name']
        description=request.POST['description']
        quantity=request.POST['quantity']
        price=request.POST['price']
        currency=request.POST['currency']
        baner_image= request.FILES['image']
        category_id=request.POST['category_id']

        images=request.FILES.getlist('images')
        product=Product.objects.create(
            name=name,
            description=description,
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
        return redirect('product')
        
    return render(request,'dashboard/product/create.html',{'category':Category.objects.all()})


def product_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.quantity = request.POST['quantity']
        product.currency = request.POST['currency']
        product.discount_price = request.POST['discount_price']
        product.baner_image = request.FILES['image']
        product.category_id = request.POST['category_id']
        
        # Yangi tasvirlarni olish
        new_images = request.FILES.getlist('images')
        
        # ProductImage instanslarini yaratish
        for new_image in new_images:
            ProductImage.objects.create(
                image=new_image,
                product=product
            )

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
    # Get the specific product based on the id parameter
    product = get_object_or_404(Product, id=id)

    user = request.user
    active_card = Card.objects.filter(user=user, is_active=True).first()

    if not active_card:
        active_card = Card.objects.create(user=user)

    # Check if the product is already in the card
    existing_product = CardProduct.objects.filter(card=active_card, product=product).first()

    if existing_product:
        # If the product is already in the card, increment the quantity
        existing_product.quantity += 1
        existing_product.save()
    else:
        # If the product is not in the card, create a new CardProduct
        CardProduct.objects.create(card=active_card, product=product, quantity=1)

    return redirect('carts')

