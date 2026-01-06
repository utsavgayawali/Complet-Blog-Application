from django.shortcuts import render
from .models import Post


def home(request):

    context={
        'post':Post.objects.all()
    }
    return render(request,'Base/home.html',context)



def About(request):
    return render(request,'Base/about.html')


def register_view(request):
    return render(request,'User/register.html')
def login_view(request):
    return render(request,'User/login.html')
def logout_view(request):
    return render(request,'User/logout.html')
def profile_view(request):
    return render(request,'User/profile.html')