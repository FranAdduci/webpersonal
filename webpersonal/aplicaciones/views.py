from django.shortcuts import render,HttpResponse
from .models import Portafolio
# Create your views here.

def home (request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")

def contact (request):
    return render (request,"contact.html")

def proyecto (request):
    portafolio= Portafolio.objects.all()
    return render (request,"proyecto.html",{'proyectos':portafolio})

def base (request):
    return render (request,"base.html")