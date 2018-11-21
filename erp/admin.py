from django.contrib import admin

# Register your models here.

from .models import Customer, Contract, Product


admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(Product)
