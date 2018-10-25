from django.db import models

# Create your models here.


class SystemMessagePush(models.Model):
    """
    系统消息推送
    """
    import_date = models.DateTimeField(max_length=19, null=False, blank=True, verbose_name="导入时间")
    company_id = models.IntegerField(null=False, blank=True, verbose_name="公司Id")
    company_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="公司名称")
    phone_pay = models.CharField(max_length=20, null=True, blank=True, verbose_name="签约用户联系手机号")
    user_id_kad = models.IntegerField(null=False, blank=True, verbose_name="kad系统用户唯一标识")
    message = models.CharField(max_length=200, null=True, blank=True, verbose_name="推送具体消息")
    is_read = models.IntegerField(null=True, blank=True, verbose_name="消息是否被查看")
    #1(已查看) 0(未查看) 2(消息失效)
    read_date = models.DateTimeField(max_length=19, null=True, blank=True, verbose_name="客服查看时间")
    reader = models.CharField(max_length=200, null=True, blank=True, verbose_name="查看人")
    is_admin_read = models.IntegerField(null=True, blank=True, verbose_name="经理是否已读")
    #1(已查看) 0(未查看) 2(消息失效)
    admin_read_date = models.DateTimeField(max_length=19, null=True, blank=True, verbose_name="经理查看时间")

    class Meta:
        db_table = "system_message_push"
        verbose_name = "系统消息推送"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message
