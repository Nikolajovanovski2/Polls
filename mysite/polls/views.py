from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my second project for my internship in Qpick")