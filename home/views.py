from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Profile
from django.contrib.auth import login,logout
from django.contrib import messages
from home.form import RegisterForm,LoginForm,ProfileupdateForm,UserUpdateForm,CreatePostForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


def home(request):
    context={
        'post':Post.objects.all()
    }
    return render(request,'Base/home.html',context)


def About(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'Base/about.html',{'post':post})


def create_post(request):
    if request.method =="POST":
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author =request.user
            post.slug=slugify(post.title)
            post.save()
            return redirect('home')
    else:
        form = CreatePostForm()

    return render(request,'Base/create_post.html',{'form':form,"title": "Create Post", "button_text": "Create Post"})

  

def edit_post(request,slug):
    post = get_object_or_404(Post,slug=slug)

    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePostForm(instance=post)

    return render(request,'Base/create_post.html',{'form':form,"title": "Edit Post", "button_text": "Update"})

 
def delete_post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request,'Base/confirm_delete.html',{'post':post})





def register_view(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Account creates Sucessfully')
            return redirect('home')
        else:
            messages.error(request,'Please fix the error below')
    else:
        form = RegisterForm()   


    return render(request,'User/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            messages.success(request,'Logged in Sucessfully')
            return redirect('home')
        else:
            messages.error(request,'Please fix the error below')
    else:
        form = LoginForm()

    return render(request,'User/login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out Sucessfully')
    return redirect(home)




@login_required
def profile_view(request):
    user = request.user
    # It tries to fetch an object from the database,If it doesn’t exist, it creates it automatically.
    profile,created = Profile.objects.get_or_create(user=user)
    context= {
        'user':user,
        'profile':profile
    }

    return render(request,'User/profile.html',context)

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(
            request.POST,
            instance= request.user
        )
        profile_form =ProfileupdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form =UserUpdateForm(instance=request.user)
        profile_form = ProfileupdateForm(instance= request.user.profile)

    context ={
        'user_form':user_form,
        'profile_form':profile_form
    }


    return render(request,'User/p_update.html',context)


