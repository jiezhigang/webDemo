# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.


def find_index(request):
    # 视图与数据分离
    context = {}
    context['hello'] = 'jiezhigang'
    return render(request, 'test.html', context)


def test_base(request):
    return render(request, 'testBase.html')
