from django.shortcuts import render


def home(request):
    return render(request,'Base/home.html')

def About(request):
    return render(request,'Base/about.html')
