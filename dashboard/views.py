from django.shortcuts import render,redirect
from main.models import Card, CardProduct, Category, Product, ProductImage, ProductReview, WishList

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
    categorys = Category.objects.all()
    context = {
        'categorys':categorys
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


