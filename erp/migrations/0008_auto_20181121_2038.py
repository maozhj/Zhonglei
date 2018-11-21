# Generated by Django 2.1.3 on 2018-11-21 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('erp', '0007_contract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': '合同', 'verbose_name_plural': '合同'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '客户', 'verbose_name_plural': '客户'},
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_name',
            field=models.CharField(max_length=50, verbose_name='合同名称'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.Customer',
                                    verbose_name='签约客户'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.IntegerField(choices=[(1, '国内'), (2, '国际'), (99, '一般')], default=1, verbose_name='客户类型'),
        ),
    ]
