from main import models
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def listproduct(request):
    products=models.Product.objects.all()
    serialazer=ProductSerializer(products, many=True)
    return Response(serialazer.data)

@api_view(["GET"])
def listcategory(request):
    categories=models.Category.objects.all()
    serialazer=CategorySerializer(categories, many=True)
    return Response(serialazer.data)

@api_view(["GET"])
def listproductimage(request):
    primages=models.ProductImage.objects.all()
    serialazer=ProductImageSerializer(primages, many=True)
    return Response(serialazer.data)


@api_view(["GET"])
def listreview(request):
    rewiews=models.ProductReview.objects.all()
    serialazer=ProductReviewSerializer(rewiews, many=True)
    return Response(serialazer.data)


@api_view(["GET"])
def listcard(request):
    cards=models.Card.objects.all()
    serialazer=CardSerializer(cards, many=True)
    return Response(serialazer.data)

@api_view(["GET"])
def listcardproduct(request):
    cardproducts=models.CardProduct.objects.all()
    serialazer=CardProductSerializer(cardproducts, many=True)
    return Response(serialazer.data)

@api_view(["GET"])
def listenterproduct(request):
    enterproducts=models.EnterProduct.objects.all()
    serialazer=EnterProductSerializer(enterproducts, many=True)
    return Response(serialazer.data)

@api_view(["GET"])
def listwishlist(request):
    wishlists=models.WishList.objects.all()
    serialazer=WishListSerializer(wishlists, many=True)
    return Response(serialazer.data)