from django.db import models
from django.contrib import admin
from .contract import Customer


class Product(models.Model):
    product_name = models.CharField('产品名称', max_length=50, null=False, blank=False)
    product_model = models.CharField('产品型号', max_length=20, null=False, blank=False)
    use_for = models.CharField('用途', max_length=30, null=True, blank=True)
    product_size = models.CharField('产品尺寸', max_length=25, null=True, blank=True)
    texture = models.CharField('材质', max_length=30, null=False, blank=False)
    volume_weight = models.IntegerField('容重', null=True, blank=True)
    piece_weight = models.FloatField('单重', null=True, blank=True)

    customer = models.ForeignKey(Customer, verbose_name='所属客户', on_delete=models.CASCADE, null=False,
                                 blank=False)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'

    def __str__(self):
        return '{0}  {1} {2}'.format(self.customer.customer_code, self.product_model, self.texture)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_model', 'texture', 'customer', 'product_size', 'volume_weight',
                    'piece_weight', 'product_name', 'use_for')
    list_display_links = ('product_model',)
    search_fields = ('customer__customer_name', 'customer__customer_code', 'product_model')

    list_filter = ('customer', 'texture')
    list_select_related = True
    list_per_page = 18
    list_max_show_all = 200
