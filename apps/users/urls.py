from django.conf.urls import url
from users import views


urlpatterns = [

    url(r'createRole/', views.create_role, name='create_role'),
    url(r'getRoles', views.get_roles, name="getRoles"),
    url(r'delRole', views.del_role, name="delRole"),
    url(r'updateRole', views.update_role, name="updateRole"),

]
