from rest_framework import serializers
from model_test.models import Test


class ModelTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'

    # name = serializers.CharField(required=True, max_length=50)
    # email = serializers.CharField(required=True, max_length=50)
    # add_time = serializers.DateTimeField(required=True)
    # update_time = serializers.DateTimeField(required=True)

