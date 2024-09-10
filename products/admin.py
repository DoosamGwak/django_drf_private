from django.contrib import admin
from .models import Product, Tag


class TagAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Product)
admin.site.register(Tag, TagAdmin)
