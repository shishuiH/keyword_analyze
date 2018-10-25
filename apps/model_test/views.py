from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .serializers import ModelTestSerializer
from .models import Test
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .filters import TestFilter
from rest_framework import filters
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
# Create your views here.


class ModelTestListView(APIView):
    """"
    测试模型列表
    """
    def get(self, request, format=None):
        list_model_test = Test.objects.all()
        list_model_test_serializer = ModelTestSerializer(list_model_test, many=True)
        return Response(list_model_test_serializer.data)


class ModelTestListView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    测试列表
    """

    queryset = Test.objects.all()
    serializer_class = ModelTestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ModelTestPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100


class ModelTestListView(generics.ListAPIView):
    """
    测试列表
    """

    queryset = Test.objects.all()
    serializer_class = ModelTestSerializer


class ModelTestListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    测试列表
    """

    queryset = Test.objects.all()
    serializer_class = ModelTestSerializer
    pagination_class = ModelTestPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TestFilter
    search_fields = ('name', 'email')
    ordering_fields = ('add_time',)


def get_data(request):

    print('test')
    return HttpResponse("success", content_type="application/json")


