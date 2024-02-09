from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Card, CardProduct, Category, Product, ProductImage, ProductReview, WishList


def index(request):
    card = Card.objects.all() 
    cardproduct = CardProduct.objects.all() 
    category = Category.objects.all() 
    product = Product.objects.all() 
    productimage = ProductImage.objects.all() 
    productreview = ProductReview.objects.all() 

    # WishList uchun is_saved qiymati olish
    is_saved = None
    # if request.user.is_authenticated:  # Foydalanuvchining tizimga kirganligini tekshirish
    #     objects = WishList.objects.filter(user=request.user)
    #     if objects.product.id==product.id:
    #         is_saved = objects.first().id
    #     else:
    #         is_saved = False


    context = {
        'card': card,
        'cardproduct': cardproduct,
        'category': category,
        'product': product,
        'productimage': productimage,
        'wishList': WishList.objects.filter(user=request.user),
        'productreview': productreview,
        'user': request.user,
        'is_saved': is_saved,
    }

    return render(request, 'index.html', context)







def card_product(request):
    card_products = CardProduct.objects.all()
    return render(request, 'index.html', {'card_products': card_products})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})




#vazifaga



def detail(request, id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=id)
    images = ProductImage.objects.filter(product_id=product.id)
    category_id = product.category.id    
    recomendation = Product.objects.filter(category_id=category_id).exclude(id=product.id)[:3]
    objects = WishList.objects.filter(user=request.user, product=product)
    is_saved = None
    if objects:
        is_saved = objects.first().id
    else:
        is_saved = False


    try: 
        a = int(request.POST.get('baho'))      
    except (TypeError, ValueError):
        a = 0

    if a > 5:
        baho = 5
    else:
        baho = a
        ProductReview.objects.create(
        user=request.user,
        product=product,
        mark=baho
    )

    context = {
        'products': products,
        'product': product,
        'images': images,
        'range': range(baho),
        'recomendation': recomendation,
        'is_saved':is_saved
    }

    return render(request, 'single.html', context)








def product_image(request):
    product_images = ProductImage.objects.all()
    return render(request, 'index.html', {'product_images': product_images})


def product_review(request):
    product_reviews = ProductReview.objects.all()
    return render(request, '.html', {'product_reviews': product_reviews})


def wishlist(request):
    wishlists = WishList.objects.all()
    return render(request, '.html', {'wishlists': wishlists})







#carts



def carts(request):
    active=Card.objects.filter(is_active=True,user=request.user)
    in_active=Card.objects.filter(is_active=False,user=request.user)
    context={
        'active':active,
        'in_active':in_active
    }
    return render(request,'cart/carts.html',context)


def cart_detail(request,id):
    cart=Card.objects.get(id=id)
    items=CardProduct.objects.filter(card=cart)

    context={
        'cart':cart,
        'items':items
    }
    return render(request,'cart/cart_detail.html',context)


def cart_detail_delete(request):
    item_id = request.GET['items_id']
    item = CardProduct.objects.get(id=item_id)
    cart_id = item.card.id
    item.delete()
    return redirect('main:cart_detail', cart_id)






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
    return redirect('main:carts')





def buy_cart(request, id):
    cart=Card.objects.get(id=id , is_active=True)
    cart_products=CardProduct.objects.filter(card=cart)
    for cart_product in cart_products:
        product=cart_product.product
        product.quantity-=cart_product.quantity
        product.save()
    cart.is_active = False
    cart.save()
    return redirect('main:carts')



def create_wishlist(request):
    WishList.objects.create(
        user=request.user,
        product_id=request.GET['product_id']
    )

    return redirect('main:index')


def list_wishlist(request):
    objects=WishList.objects.filter(user=request.user)
    return render(request, 'wish/list.html', {'objects':objects})



def delete_wish(request):
    wish= WishList.objects.get(id=request.GET['id'])
    wish.delete()
    return redirect('main:list_wishlist')

















    







