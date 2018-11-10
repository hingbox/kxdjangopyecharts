# -*- coding: utf-8 -*-
#encoding=utf-8
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
def index(request):
    #request.POST
    #request.GET
    # return HttpResponse("hello word!")
    return render(request, "index.html")