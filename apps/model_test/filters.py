from django_filters import rest_framework as filters

from .models import Test


class TestFilter(filters.FilterSet):
    """
    测试的过滤类
    """

    class Meta:
        model = Test
        fields = ['name', 'email']
