from django.db import models
from .contract import Contract


class Product(models.Model):
    Product_name = models.CharField('合同名称', max_length=50, null=False, blank=False)
    contract = models.ForeignKey(Contract, default=1,on_delete=models.CASCADE, null=False, blank=False)
    date_signed = models.DateField('签字日期', null=False, blank=False)
    delivery_date = models.DateField('交货日期', null=False, blank=False)
    contract_code = models.CharField('合同编号', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = '合同'

    def __str__(self):
        return self.contract_name

