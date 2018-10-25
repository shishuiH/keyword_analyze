#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import SystemMessagePush
from xadmin import views


class SystemMessagePushAdmin(object):
    list_display = ["company_name", "phone_pay", "message", "reader"]   #控制显示的列
    search_fields = ["company_name", "phone_pay", "message", "reader"]  #控制搜索的列
    list_filter = ["company_name", "phone_pay", "message", "reader"]    #控制过滤的列

    def queryset(self):     #查询语句
        qs = super(SystemMessagePushAdmin, self).queryset()
        qs = qs.filter(is_read=0, is_admin_read=0, user_id_kad=271)
        return qs


xadmin.site.register(SystemMessagePush, SystemMessagePushAdmin)     #注册到xadmin管理


