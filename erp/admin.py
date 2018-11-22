from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Worker, WorkerAdmin)
