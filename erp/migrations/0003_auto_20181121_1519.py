# Generated by Django 2.1.3 on 2018-11-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20181121_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, null=1, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact_name',
            field=models.CharField(max_length=20, null=1, verbose_name='联系人'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_code',
            field=models.CharField(max_length=5, null=0, verbose_name='客户代码'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(max_length=50, null=0, verbose_name='客户名称'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50, null=1, verbose_name='电子邮件'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tel',
            field=models.CharField(max_length=20, null=1, verbose_name='电话'),
        ),
    ]