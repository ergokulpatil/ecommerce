from django.contrib import admin
from .models import Customer, Product,Cart,OrderPlaced
# Register your models here.

@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','name','locality','city','zipcode','state']


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['title','selling_price','discounted_price','description','brand','category','product_image']


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class AdminOrderPlaced(admin.ModelAdmin):
    list_display = ['id','customer','product','quantity','ordered_date','status']

