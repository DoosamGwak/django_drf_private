from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductRetrieveUpdateDestroyView,
    ProductLikeView,
)


urlpatterns = [
    path("list/", ProductListView.as_view(), name="product_list"),
    path("", ProductCreateView.as_view(), name="product_create"),
    path(
        "<int:pk>/", ProductRetrieveUpdateDestroyView.as_view(), name="product_detail"
    ),
    path("<int:pk>/like/", ProductLikeView, name="product_detail"),
]
