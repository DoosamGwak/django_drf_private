from rest_framework import serializers
from .models import Product


class ProductDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = (
            "id",
            "author",
            "created_at",
            "updated_at",
            "followings",
            "user_likes",
        )


class ProductListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "author",
            "title",
            "tags",
            "like_count",
        )
