from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)


class Product(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name="product",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/no_image.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user_likes = models.ManyToManyField(
        get_user_model(), related_name="product_likes", blank=True
    )
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
