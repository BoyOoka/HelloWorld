# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
# from django


# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search_get(request):
    print(request)
    print(request.GET)
    request.encoding = 'utf-8'
    if request.GET['q']:
        message = '你搜索的内容为：' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


def search_post(request):
    print(request)
    print(request.POST)
    if request.POST['q']:
        message = '你提交的内容为：' + request.POST['q']
    else:
        message = '你提交了空内容'
    return HttpResponse(message)
