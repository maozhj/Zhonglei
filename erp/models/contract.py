from django.db import models
from django.contrib import admin

from .customer import Customer


class Contract(models.Model):
    contract_name = models.CharField('合同名称', max_length=50, null=False, blank=False)
    customer = models.ForeignKey(Customer, verbose_name = '签约客户', default=1, on_delete=models.CASCADE, null=False, blank=False)
    date_signed = models.DateField('签字日期', null=True, blank=True)
    delivery_date = models.DateField('交货日期', null=True, blank=True)
    contract_code = models.CharField('合同编号', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = '合同'

    def __str__(self):
        return self.contract_name


class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_name', 'customer', 'date_signed', 'delivery_date', 'contract_code')
    search_fields = ('contract_name', 'customer__customer_name', 'customer__customer_code')
