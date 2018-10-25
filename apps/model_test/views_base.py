from django.shortcuts import render
from django.views.generic.base import View
from .models import Test


# Create your views here.


class ModelTestListView(View):
    def get(self, request):
        # 通过django的view实现测试模型列表页
        """
        展示测试模型列表
        :param request:
        :return:
        """
        json_list = list()
        list_model_test = Test.objects.all()[:10]
        # for test in list_model_test:
        #     json_dict = dict()
        #     json_dict["name"] = test.name
        #     json_dict["email"] = test.email
        #     json_list.append(json_dict)

        from django.core import serializers
        from django.http import JsonResponse
        import json

        json_data = serializers.serialize('json', list_model_test)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
