
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    register_time = models.DateField(max_length=19, null=True, blank=True, verbose_name="注册时间")
    update_time = models.DateTimeField(max_length=19, null=True, blank=True, verbose_name="更新时间")
    employee_name = models.CharField(max_length=50, null=False, blank=True, verbose_name="员工昵称")
    employee_number = models.CharField(max_length=50, null=False, blank=True, verbose_name="员工编号")
    user_state = models.CharField(max_length=50, null=True, blank=True, verbose_name="用户状态")
    remark = models.CharField(max_length=200, null=True, blank=True, verbose_name="备注")

    class Meta:
        db_table = 'user'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色
    """
    role_name = models.CharField(max_length=50, null=False, blank=True, verbose_name="角色昵称")
    add_time = models.DateTimeField(max_length=19, null=True, blank=True, verbose_name="添加时间")
    update_time = models.DateTimeField(max_length=19, null=True, blank=True, verbose_name="更新时间")

    class Meta:
        db_table = 'role'
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.role_name


class UserRole(models.Model):
    """
    用户角色
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="角色")

    class Meta:
        db_table = 'user_role'
        verbose_name = "用户角色"
        verbose_name_plural = verbose_name
