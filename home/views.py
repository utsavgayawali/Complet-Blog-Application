from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages




def home(request):

    context={
        'post':Post.objects.all()
    }
    return render(request,'Base/home.html',context)

def About(request):
    return render(request,'Base/about.html')




def register_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Account creates Sucessfully')
            return redirect(home)
        else:
            messages.error(request,'Please fix the error below')
    else:
        form = UserCreationForm()   


    return render(request,'User/register.html',{'form':form})





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            messages.success(request,'Logged in Sucessfully')
            return redirect(home)
        else:
            messages.error(request,'Please fix the error below')
    else:
        form = AuthenticationForm()

    return render(request,'User/login.html',{'form':form})





def logout_view(request):
    logout(request)
    messages.success(request,'Logged out Sucessfully')
    return redirect(home)





def profile_view(request):
    return render(request,'User/profile.html')