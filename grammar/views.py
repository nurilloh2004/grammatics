from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render( request,'main/home.html')

def addcard(request):
    return render(request, 'main/addcard.html')