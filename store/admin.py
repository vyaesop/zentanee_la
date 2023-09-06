from django.contrib import admin
from .models import Address, Category, Product, Cart, Order, ProductImages, Brand, Coupon

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'phone')
    list_filter = ('city', 'phone')
    list_per_page = 10
    search_fields = ('address', 'city', 'phone')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}

class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'brand_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    
    list_display = ('title', 'slug', 'category','brand', 'product_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'category','brand', 'is_active', 'is_featured')
    list_filter = ('category','brand', 'is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'category', 'short_description')
    prepopulated_fields = {"slug": ("title", )}

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')
    
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code','active', 'discount', 'active_date', 'expiry_date', 'created_date')
    # list_editable = ('code','active', 'discount', 'active_date', 'expiry_date', 'created_date')
    list_per_page = 20

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user', 'product')
    
 

admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)