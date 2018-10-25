from django.shortcuts import render

# Create your views here.
import requests, json


def company_account_info(request):
    """
    获取公司账户信息
    :param request:
    :return:
    """
    requests_url = 'https://pre-release.nisure.net/keyword-analyze/companyController.do?getCompanysByParam'
    data = json.dumps({'search': 'companyName', 'searchType': 'companyName', 'pageNumber': 1, 'pageSize': 10})
    back = requests.post(requests_url, data, auth=('kadadmin', 'lPn8jxk9XT6IFqGm'))
    print(back.json)


