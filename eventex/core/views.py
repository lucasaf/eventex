# coding: utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse
from django.template import loader, Context


def home(request):
    return render(request, 'index.html')
