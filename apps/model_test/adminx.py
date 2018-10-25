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
from model_test.models import Test
from xadmin import views


class TestAdmin(object):
    list_display = ["name", "email", "add_time", "update_time"]
    search_fields = ["name", "email", "add_time", "update_time"]
    list_filter = ["name", "email", "add_time", "update_time"]


xadmin.site.register(Test, TestAdmin)


