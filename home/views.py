from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'home.html')

