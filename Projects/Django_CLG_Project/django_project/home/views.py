from cgitb import html
import email
from operator import concat
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html', )
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html', )
    #return HttpResponse("This is services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'contact.html', )
   # return HttpResponse("This is contact page")

def Icecream(request):
    return render(request, 'IceCream.html', )
    #return HttpResponse("This is Ice-Cream page")

def FamilyPack(request):
    return render(request, 'FamilyPack.html', )
   # return HttpResponse("This is Family Pack page")
