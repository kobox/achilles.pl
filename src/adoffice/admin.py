from django.contrib import admin
from .models import Category, GroupCategory, Product, ProductImage, Finishing, Accessories


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'slug', 'header',)

    model = Category

@admin.register(GroupCategory)
class GroupCategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title',)

    model = GroupCategory

@admin.register(Finishing)
class FinishingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title',)

    model = Finishing

@admin.register(Accessories)
class FinishingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title',)

    model = Accessories

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title',)

    model = Product

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'picture',)

    model = ProductImage