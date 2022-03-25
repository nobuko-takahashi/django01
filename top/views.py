#from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'top/index.html',
        context={}
    )
