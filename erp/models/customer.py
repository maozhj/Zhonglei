from django.db import models


class Customer(models.Model):
    customer_type_list = (
        (1, '国内'),
        (2, '国际'),
        (99, '一般'),
    )
    customer_name = models.CharField('客户名称', max_length=50, null=False, blank=False)
    customer_type = models.IntegerField('客户类型', choices=customer_type_list, default=1, null=False, blank=False)
    customer_code = models.CharField('客户代码', max_length=5, null=False, blank=False)
    contact = models.CharField('联系人', max_length=20, null=True, blank=True)
    address = models.CharField('地址', max_length=100, null=True, blank=True)
    tel = models.CharField('电话', max_length=20, null=True, blank=True)
    email = models.EmailField('电子邮件', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户'

    def __str__(self):
        return '{0} - {1}'.format(self.customer_code, self.customer_name)
