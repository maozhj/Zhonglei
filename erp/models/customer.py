from django.db import models


class Customer(models.Model):
    customer_type_list = (
        (1, '国内'),
        (2, '国际'),
        (99, '一般'),
    )
    customer_name = models.CharField('客户名称', max_length=50, null=False, blank=False)
    customer_type = models.IntegerField(choices=customer_type_list, default=1, null=False, blank=False)
    customer_code = models.CharField('客户代码', max_length=5, null=False, blank=False)
    contact = models.CharField('联系人', max_length=20, null=True, blank=True)
    address = models.CharField('地址', max_length=100, null=True, blank=True)
    tel = models.CharField('电话', max_length=20, null=True, blank=True)
    email = models.EmailField('电子邮件', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = '客户'

    def __str__(self):
        return '{0} - {1}'.format(self.customer_code, self.customer_name)






# CREATE TABLE `PRODUCTS` (
#   `PRODUCTID` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `PRODUCTNAME` varchar(45) COLLATE utf8_bin DEFAULT NULL,
#   `PRODUCTMODEL` varchar(45) COLLATE utf8_bin DEFAULT NULL,
#   `USEFOR` varchar(45) COLLATE utf8_bin DEFAULT NULL,
#   `PRODUCTSIZE` varchar(45) COLLATE utf8_bin DEFAULT NULL,
#   `TEXTURE` varchar(20) COLLATE utf8_bin DEFAULT NULL,
#   `VOLUMEWEIGHT` decimal(6,2) DEFAULT NULL COMMENT '体积重量(容重)',
#   `PIECEWEIGHT` decimal(4,2) DEFAULT NULL,
#   `CONTRACTID` int(11) DEFAULT NULL,
#   `ORDERQUANTITY` int(10) DEFAULT NULL,
#   `CREATEDATE` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
#   `UPDATEDATE` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#   PRIMARY KEY (`PRODUCTID`),
#   KEY `FK_PRODUCTS_CONTRACTID_idx` (`CONTRACTID`),
#   CONSTRAINT `FK_PRODUCTS_CONTRACTID` FOREIGN KEY (`CONTRACTID`) REFERENCES `CONTRACTS` (`CONTRACTID`)
# ) ENGINE=InnoDB AUTO_INCREMENT=268 DEFAULT CHARSET=utf8 COLLATE=utf8_bin