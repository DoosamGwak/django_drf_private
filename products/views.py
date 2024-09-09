from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .paginations import StandardResultsSetPagination
from .permissions import OwnerOnly
from .serializers import (
    ProductDetailSerializer,
    ProductListSerializer,
)


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product
    permission_classes = (
        IsAuthenticated,
        OwnerOnly,
    )
    serializer_class = ProductDetailSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.annotate(like_count=Count("user_likes"))
    serializer_class = ProductListSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "content"]


class ProductLikeView(APIView):
    permission_classes = (
        IsAuthenticated,
        OwnerOnly,
    )

    def post(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
