# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from demo import tasks


def task1(request):
    tasks.demo_task1.delay()
    print("added\n\n")
    return render(request, 'demo/task1.html')

