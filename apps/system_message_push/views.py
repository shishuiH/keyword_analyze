from django.views.generic import View
from .models import SystemMessagePush
from rest_framework.views import APIView
from .serializers import SystemMessagePushSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filter import SystemMessagePushFilter
from rest_framework import filters
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
import datetime


class SystemMessagePushListView(View):
    """
    这种写法会导致时间和相片路径数据不能序列化
    """
    # def get(self, request):
    #     """
    #    通过django的djangoview实现信息列表
    #     """
    #     json_list = []
    #     messages = SystemMessagePush.objects.all()
    #
    #     from django.forms.models import model_to_dict
    #     for message in messages:
    #         json_dict = model_to_dict(message)
    #         json_list.append(json_dict)
    #
    #     from django.http import HttpResponse
    #     import json
    #     return HttpResponse(json.dumps(json_list), content_type='application/json')
    def get(self, request):
        json_list = []
        messages = SystemMessagePush.objects.all()
        import json
        from django.core import serializers
        from django.http import JsonResponse

        json_data = serializers.serialize('json', messages)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)


class SystemMessagePushListView(APIView):
    """
    消息列表
    """
    def get(self, request, format=None):
        messages = SystemMessagePush.objects.all()
        messages_serializer = SystemMessagePushSerializer(messages, many=True)
        return Response(messages_serializer.data)


class SystemMessagePushListView(generics.ListAPIView):
    """
    消息列表
    """
    queryset = SystemMessagePush.objects.all()
    serializer_class = SystemMessagePushSerializer


class SystemMessagePushPagingation(PageNumberPagination):
    """
    消息列表自定义分页
    """
    #默认分页显示的个数
    page_size = 15
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 1000


class SystemMessagePushListView(generics.ListAPIView):
    """
    消息列表
    """

    pagination_class = SystemMessagePushPagingation
    queryset = SystemMessagePush.objects.all().order_by('id')
    serializer_class = SystemMessagePushSerializer


class SystemMessagePushListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    消息列表
    """
    queryset = SystemMessagePush.objects.all().filter(user_id_kad=271, is_read=0).order_by('id')
    pagination_class = SystemMessagePushPagingation
    serializers_class = SystemMessagePushSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    #设置filter的类为我们自定义的类
    filter_class = SystemMessagePushFilter
    #搜索，“=”表示精确搜索，也可以使用正则表达式
    search_fields = ('company_name', 'phone_pay')
    #排序
    ordering_fields = ('company_name',)


import json


from django.shortcuts import render
# from MySQLdb import cursors

# Create your views here.


#打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "ysanalyze", "utf8")

#使用cursor方法获取操作游标
# cursor = db.cursor()

#sql 查询语句
def sys_test(request):
    cursor = connection.cursor()

    sql = "SELECT id, company_name, message FROM system_message_push_systemmessagepush LIMIT 0, 10"

    try:
        #执行sql语句
        cursor.execute(sql)
        #获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            r_id = row[0]
            compnay_name = row[1]
            message = row[2]
            #打印结果
            print("公司名称=%s, 消息=%s" % (compnay_name, message))

    except:
        print("error: unable to fecth data")

    #关闭数据库连接
    # db.close()
    return HttpResponse(results)


def read(request):
    print('read message')
    print(request.body)
    received_json_data = json.loads(request.body)
    page_number = received_json_data.get("params").get("page_num")
    page_size = received_json_data.get("params").get("page_size")
    search_word = received_json_data.get("params").get("select_word")

    message_list = []

    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    if search_word == '':
        messages = SystemMessagePush.objects.filter(user_id_kad=271, is_read=0).order_by('id')[start_index:end_index]
        total = len(SystemMessagePush.objects.filter(user_id_kad=271, is_read=0).order_by('id'))
    else:
        messages = SystemMessagePush.objects.filter(user_id_kad=271, is_read=0, company_name__contains=search_word).order_by('id')[start_index:end_index]
        total = len(SystemMessagePush.objects.filter(user_id_kad=271, is_read=0, company_name__contains=search_word).order_by('id'))

    for msg in messages:
        json_dict = dict()
        json_dict["id"] = msg.id
        json_dict["company_name"] = msg.company_name
        json_dict["phone_pay"] = msg.phone_pay
        json_dict["message"] = msg.message
        json_dict["reader"] = msg.reader
        message_list.append(json_dict)
    try:
        res = {
            "code": 200,
            "list": message_list,
            "total": total
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def search_message(request):
    print("search message")
    received_json_data = json.loads(request.body)
    page_number = received_json_data.get("params").get("page_num")
    page_size = received_json_data.get("params").get("page_size")
    search_word = received_json_data.get("params").get("select_word")

    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    messages = SystemMessagePush.objects.filter(user_id_kad=271, is_read=0, company_name__contains=search_word).order_by('id')[start_index:end_index]
    total = len(SystemMessagePush.objects.filter(user_id_kad=271, is_read=0, company_name__contains=search_word).order_by('id'))
    message_list = []

    for msg in messages:
        json_dict = dict()
        json_dict["id"] = msg.id
        json_dict["company_name"] = msg.company_name
        json_dict["phone_pay"] = msg.phone_pay
        json_dict["message"] = msg.message
        json_dict["reader"] = msg.reader
        message_list.append(json_dict)

    try:
        res = {
            "code": 200,
            "list": message_list,
            "total": total
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def sign_read(request):
    print("sign read")
    received_json_data = json.loads(request.body)
    record_id = received_json_data.get("params").get("id")
    print(record_id)
    message = SystemMessagePush.objects.get(id=record_id)
    message.is_read = 1
    message.read_date = datetime.datetime.now()
    message.save()

    try:
        res = {
            "code": 200,
            "msg": "已标记"
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def sign_batch(request):
    print("sign batch")
    received_json_data = json.loads(request.body)
    ids = received_json_data.get("params").get("ids")
    # ids_string = ','.join(ids)
    ids_string = ','.join(str(i) for i in ids)
    print(ids_string)
    try:
        SystemMessagePush.objects.extra(where=['id IN (' + ids_string + ')']).update(is_read=1, read_date=datetime.datetime.now())
        res = {
            "code": 200,
            "msg": "已标记"
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

