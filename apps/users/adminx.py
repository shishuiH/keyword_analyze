#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""

import xadmin
from users.models import UserProfile, UserRole, Role
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "关键词分析决策系统"
    site_footer = "原昇科技"
    menu_style = "accordion"


class UserProfileAdmin(object):
    list_display = ["username", "register_time", "update_time", "employee_name", "employee_number", "user_state", "remark"]
    search_fields = ["username", "register_time", "update_time", "employee_name", "employee_number", "user_state", "remark"]
    list_filter = ["username", "register_time", "update_time", "employee_name", "employee_number", "user_state", "remark"]


# class UserRoleAdmin(object):
#         list_display = ["user", "role"]
#         search_fields = ["user", "role"]
#         list_filter = ["user", "role"]


class RoleAdmin(object):
        list_display = ["role_name", "add_time", "update_time"]
        search_fields = ["role_name", "add_time", "update_time"]
        list_filter = ["role_name", "add_time", "update_time"]


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Role, RoleAdmin)



