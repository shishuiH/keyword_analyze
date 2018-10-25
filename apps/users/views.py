import json
import datetime


from users.models import Role
from django.utils import timezone
from django.http import HttpResponse


def create_role(request):
    print('create role')
    obj = json.loads(request.body)
    role_name = obj['role_name']

    try:
        role = Role(role_name=role_name, add_time=timezone.now(), update_time=timezone.now())
        role.save()
        res = {
            "code": 200,
            "id": role.id
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def get_roles(request):
    print('read role')
    print(request.body)
    received_json_data = json.loads(request.body)
    page_number = received_json_data.get("params").get("page_num")
    page_size = received_json_data.get("params").get("page_size")
    search_word = received_json_data.get("params").get("select_word")

    role_list = []

    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    try:

        if search_word == '':
            roles = Role.objects.order_by('-id')[start_index:end_index]
            total = len(Role.objects.order_by('-id'))
        else:
            roles = Role.objects.filter(company_name__contains=search_word).order_by('-id')[start_index:end_index]
            total = len(Role.objects.filter(company_name__contains=search_word).order_by('-id'))

        for role in roles:
            json_dict = dict()
            json_dict["id"] = role.id
            json_dict["role_name"] = role.role_name
            json_dict["update_date"] = role.update_time.strftime('%Y-%m-%d %H:%M:%S')
            role_list.append(json_dict)

        res = {
            "code": 200,
            "list": role_list,
            "total": total
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def del_role(request):
    print("sign read")
    received_json_data = json.loads(request.body)
    role_id = received_json_data.get("params").get("id")
    try:
        role = Role.objects.get(id=role_id)
        role.delete()
        res = {
            "code": 200,
            "msg": "已标记"
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def update_role(request):
    print('update role')
    obj = json.loads(request.body)
    role_id = obj['id']
    role_name = obj['role_name']

    try:
        role = Role.objects.get(id=role_id)
        role.role_name = role_name
        role.update_time = datetime.datetime.now()
        role.save()
        res = {
            "code": 200,
            "id": role.id
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")