from django.db import models
from django.contrib import admin


class Worker(models.Model):
    worker_type_list = (
        ('01', '装窑工'),
        ('02', '烧窑工'),
        ('03', '成型工'),
        ('04', '拌料工'),
        ('05', '压砖工'),
        ('06', '切割工'),
        ('07', '勤杂工'),
        ('08', '挤砖工'),
        ('99', '其他'),
    )
    worker_name = models.CharField('工人姓名', max_length=50, null=False, blank=False)
    worker_type = models.CharField('工人类型', max_length=2, choices=worker_type_list, null=False, blank=False)
    comment = models.TextField('其他说明', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = '工人'
        verbose_name_plural = '工人'

    def __str__(self):
        return self.worker_name


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('worker_name', 'worker_type', 'comment')
    list_display_links = ('worker_name', 'worker_type', 'comment')
    search_fields = ('worker_name',)
    list_filter = ('worker_type',)
    list_select_related = True
    list_per_page = 18
    list_max_show_all = 200
