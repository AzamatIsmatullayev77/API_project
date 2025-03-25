from django.contrib import admin

from texnomart.models import Product, Category, Comment


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Product, )
admin.site.register(Category, ProductAdmin)
admin.site.register(Comment)
