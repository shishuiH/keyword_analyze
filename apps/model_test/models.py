from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="姓名")
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name="邮箱")
    add_time = models.DateTimeField(max_length=19, null=True, blank=True, verbose_name="添加时间")
    update_time = models.DateTimeField(max_length=19, null=True, blank=True, verbose_name="更新时间")

    class Meta:
        db_table = "models_test"
        verbose_name = "测试模型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


