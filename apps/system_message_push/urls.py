from django.conf.urls import url
from system_message_push import views


urlpatterns = [
    # url(r'get_test$', views.get_data, ),
    url('readMessage', views.read, name='readSystemMessage'),
    url('searchMessage', views.search_message, name='searchMessage'),
    url('signRead', views.sign_read, name='signRead'),
    url('signBatch', views.sign_batch, name='signBatch'),
]
