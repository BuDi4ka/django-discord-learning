from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Home Page')


def room(request):
    return HttpResponse('Room') 