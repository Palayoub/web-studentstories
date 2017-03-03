from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('home/index.html')
    context = {
            'variable': "randomVaribale",
            }
    return HttpResponse(template.render(context, request))
# Create your views here.

