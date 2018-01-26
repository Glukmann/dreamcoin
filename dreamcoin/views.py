# -*- coding: utf-8 -*-
import os
import csv
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404



def home(request):
    return render(request, 'index.html', {})
# -*- coding: utf-8 -*-


