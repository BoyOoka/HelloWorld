# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World !'
    # return HttpResponse("Hello world !")
    return render(request, 'hello.html', context)
