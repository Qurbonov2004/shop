from rest_framework import serializers
from main import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields='__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductImage
        fields='__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductReview
        fields='__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Card
        fields='__all__'


class CardProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CardProduct
        fields='__all__'

class EnterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.EnterProduct
        fields='__all__'


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.WishList
        fields='__all__'