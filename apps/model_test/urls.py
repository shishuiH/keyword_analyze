from django.conf.urls import url,include
from model_test import views


urlpatterns = [
    url(r'get_test/', views.get_data, name='get_test'),
]
