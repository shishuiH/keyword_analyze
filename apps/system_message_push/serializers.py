# author by shishui
from rest_framework import serializers
from .models import SystemMessagePush


# class SystemMessagePushSerializer(serializers.Serializer):
#     import_date = serializers.DateTimeField(required=True)
#     company_id = serializers.IntegerField(default=0)
#     company_name = serializers.CharField(required=True)
#     phone_pay = serializers.CharField(required=True)
#     user_id_kad = serializers.IntegerField(default=0)
#     message = serializers.CharField(required=True)
#     is_read = serializers.IntegerField(default=0)
#     read_date = serializers.DateTimeField(required=True)
#     is_admin_read = serializers.IntegerField(default=0)
#     admin_read_date = serializers.DateTimeField(required=True)
class SystemMessagePushSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMessagePush
        fields = '__all__'
