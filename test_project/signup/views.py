from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student

def index(request):
    template = loader.get_template('home/signup.html')
    context = { 'variable': "BOUUHHHH" }
    return HttpResponse(template.render(context, request))
def check(request):
    #students = Student.objects.all()
    user = request.POST['username']
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    civ = request.POST['civilite']
    em = request.POST['email']
    passw = request.POST['password']
    if civ == 'M':
        c = True
    else:
        c = False
    query = Student(username=user, first_name=prenom, last_name=nom, civilite=c, email=em, password=passw)
    query.save()
    context = { 'user': user }
    return render(request, 'home/check.html', context)
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


# Create your views here.

