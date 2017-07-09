from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from signup.models import Student
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView

def index(request):
    template = loader.get_template('home/index.html')
    context = {
            'variable': "randomVaribale",
            }
    return HttpResponse(template.render(context, request))
# Create your views here.


def connect(request):
    user = request.POST['username']
    passw = request.POST['passwrd']
    try:
    	listing = Student.objects.get(username=user , password=passw)
    except Student.DoesNotExist:
    	listing = 0
    context = { 'user' : user,
    'passwrd' : passw,
    'listing' : listing}
    return render(request,'home/connect.html',context)
'''

class LoginView(TemplateView):
    template_name = 'home/index.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('passwrd', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect( 'home/connect.html' )
        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'home/index.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

       '''