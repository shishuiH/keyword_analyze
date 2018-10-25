from django.db import models

# Create your models here.


class CompanyAccountInfo(models.Model):
    """
    公司账户信息
    """
    industry = models.CharField(max_length=20, verbose_name="所属行业")
    industry_id = models.CharField(max_length=32, verbose_name="行业id")
    username = models.CharField(max_length=20, verbose_name="运营专员")
    register_time = models.DateTimeField(verbose_name="注册时间")
    company_name = models.CharField(max_length=50, verbose_name="代运营公司名称")
    customer_name = models.CharField(max_length=20, verbose_name="客户姓名")
    phone = models.CharField(max_length=20, verbose_name="代运营公司电话")
    email = models.CharField(max_length=20, verbose_name="电子邮件")
    address = models.CharField(max_length=100, verbose_name="公司地址")
    postcard = models.CharField(max_length=20, verbose_name="邮编")
    company_state = models.CharField(max_length=20, verbose_name="代运营公司状态")
    company_state_value = models.CharField(max_length=20, verbose_name="公司状态、即续费状态")
    user_id = models.IntegerField(verbose_name="用户id")
    is_has_baidu_data = models.CharField(max_length=20, verbose_name="该公司是否存在百度数据")
    contract_count = models.IntegerField(verbose_name="录入合同次数")
    is_has_account = models.CharField(max_length=20, verbose_name="改账户是否有百度账号")
    login_name = models.CharField(max_length=20, verbose_name="代运营公司的登录账号")
    login_password = models.CharField(max_length=20, verbose_name="代运营公司的登录密码")
    account_state = models.CharField(max_length=20, verbose_name="账户属性")
    type_tag = models.CharField(max_length=20, verbose_name="平台标签")
    sem_plat_from_name = models.CharField(max_length=20, verbose_name="平台名称")
    hit_avg_price = models.DecimalField(decimal_places=2, max_digits=2, verbose_name="平均点击价格cpc")
    bind_phone = models.CharField(max_length=20, verbose_name="绑定手机")
    budget_day = models.DecimalField(decimal_places=2, max_digits=2, verbose_name="日预算")
    advertisement_online_date = models.DateTimeField(verbose_name="广告上线时间")
    advertisement_offline_date = models.DateTimeField(verbose_name="广告到期时间")
    remark = models.CharField(max_length=20, verbose_name="备注信息")
    token = models.CharField(max_length=20, verbose_name="权限代码")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    identity = models.CharField(max_length=20, verbose_name="")
    creater = models.CharField(max_length=20, verbose_name="")
    yisheng_user_id = models.CharField(max_length=20, verbose_name="用于接受yishenguser表的id")
    company_id = models.IntegerField(verbose_name="公司id")
    if_configed = models.CharField(max_length=20, verbose_name="是否配置了权限代码")
    start_or_close = models.CharField(max_length=20, verbose_name="自动调价状态信息")
    states = models.CharField(max_length=20, verbose_name="状态")
    is_fonfig_token = models.CharField(max_length=20, verbose_name="是否配置权限代码标志")
    mainbussiness = models.CharField(max_length=20, verbose_name="主营业务")
    mb_id = models.CharField(max_length=20, verbose_name="主营业务id")
    pay_status = models.CharField(max_length=20, verbose_name="付费状态")
    mobile = models.CharField(max_length=20, verbose_name="电话")

    class Meta:
        db_table = "company_account"
        verbose_name = "公司账户信息管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_name


class AccountInfo(models.Model):
    """
    账户信息
    """
    login_name = models.CharField(max_length=20, verbose_name="代运营公司的登录账号")
    login_password = models.CharField(max_length=20, verbose_name="代运营公司的登录密码")
    account_state = models.CharField(max_length=20, verbose_name="账户属性")
    type_tag = models.CharField(max_length=20, verbose_name="平台标签")
    sem_plat_form_name = models.CharField(max_length=20, verbose_name="平台属性")
    company_name = models.CharField(max_length=50, verbose_name="公司名称")
    company_id = models.CharField(max_length=20, verbose_name="公司id")

    class Meta:
        db_table = "account_info"
        verbose_name = "账户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.login_name

