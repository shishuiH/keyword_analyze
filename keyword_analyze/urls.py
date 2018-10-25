"""keyword_analyze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from model_test.views import ModelTestListViewSet
# from model_test.views_base import ModelTestListView
from rest_framework.documentation import include_docs_urls
from model_test.views import ModelTestListViewSet
from rest_framework.routers import DefaultRouter
import xadmin
from system_message_push.views import SystemMessagePushListView
from system_message_push.views import SystemMessagePushListViewSet
from system_message_push import views as sys_views
from company_account import views as company_views
from rest_framework.authtoken import views
#利用TemplateView
from django.views.generic import TemplateView
import model_test.urls
import system_message_push.urls
import users.urls


model_test_list = ModelTestListViewSet.as_view({
    'get': 'list',
})


router = DefaultRouter()

#配置测试model的url
router.register(r'model_test', ModelTestListViewSet)
router.register(r'systemMessagePushs', SystemMessagePushListViewSet)

urlpatterns = (
    url(r'^xadmin/', xadmin.site.urls),

    # url(r'^/*', xadmin.site.urls),
    path('docs', include_docs_urls(title='关键词分析决策系统')),
    # path('api-auth/', include('rest_framework.urls')),

    #我们drf的页面中右上角的log in为什么可以实现登录
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),

    # path('model_test/', ModelTestListView.as_view(), name='model_test-list'),
    # path('model_test/', model_test_list, name='model_test-list'),
    # url(r'^model_test/$', model_test_list, name='model_test-list')
    url(r'^systemMessagePushs/', SystemMessagePushListView.as_view(), name='system_message_push-list'),

    # path('companyAccountInfo/', company_views.company_account_info, name='getCompanyAccountInfo'),

    path('sys_test/', sys_views.sys_test, name='usysTest'),


    url(r'^api/', include(model_test.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    #引入用到app的路由
    # url(r'^', include(router.urls)),
    url(r'', include(system_message_push.urls)),
    url(r'', include(users.urls)),

)
