from django_filters import rest_framework as filters
from .models import SystemMessagePush

#自定义的一个过滤器


class SystemMessagePushFilter(filters.FilterSet):
    """
    消息列表过滤器
    """

    class Meta:
        model = SystemMessagePush
        fields = ['company_name', 'phone_pay']
