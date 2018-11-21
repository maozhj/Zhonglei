from django.db import models
from .contract import Customer


class Product(models.Model):
    product_name = models.CharField('产品名称', max_length=50, null=False, blank=False)
    product_model = models.CharField('产品型号', max_length=20, null=False, blank=False)
    use_for = models.CharField('用途', max_length=30, null=True, blank=True)
    product_size = models.CharField('产品尺寸', max_length=25, null=True, blank=True)
    texture = models.CharField('材质', max_length=30, null=False, blank=False)
    volume_weight = models.FloatField('容重', null=True, blank=True)
    piece_weight = models.FloatField('单重', null=True, blank=True)
    order_quantity = models.IntegerField('订单数量', null=True, blank=True)

    Customer = models.ForeignKey(Customer, verbose_name='所属客户', default=1, on_delete=models.CASCADE, null=False,
                                 blank=False)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'

    def __str__(self):
        return '{0}  {1} {2}'.format(self.Customer.customer_code, self.product_model, self.texture)
