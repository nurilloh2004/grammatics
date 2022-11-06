from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(request):
    card = Card.objects.all()
    context = {'card': card}
    return render( request,'main/home.html', context=context)

def addcard(request):
    return render(request, 'main/addcard.html')