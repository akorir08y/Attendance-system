from django.shortcuts import render,redirect,reverse
from TTU_SYSTEM.forms import (EditProfileForm1,StdRegForm,UserProfileForm)
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from ..decorators import student_required
from TTU_SYSTEM.models import CustomUser

def home(request):
    return render('home1/home1.html')

def gallery(request):
    return render(request,'TTU_SYSTEM/gallery.html')


def register(request):
    if request.method =='POST':
        form = StdRegForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('TTU_SYSTEM:login_success')

    else:
        form = StdRegForm()

    context = {'form':form}
    return render(request, 'TTU_SYSTEM/StdReg.html',context)

def create_profile(request):
    return render(request,'TTU_SYSTEM/createprofile.html')

def user_profileform(request):
    if request.method =='POST':
        form = UserProfileForm(request.POST)
        if form.is_multipart(request.POST,request.FILES):
            form.save()
            return redirect ('home1')
    else:
        form = UserProfileForm()

    context = {'form':form}
    return render(request,'TTU_SYSTEM/std_profileform.html',context)


def view_profile(request):

    context = {'user':request.user}
    return render(request, 'TTU_SYSTEM/profile.html',context)

def view_profile_with_pk(request,id=None):
    if id:
        user = CustomUser.objects.get(id=id)
    else:
        user = request.user
    context = {'user':request.user}
    return render(request, 'TTU_SYSTEM/profile_with_pk.html',context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm1(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = EditProfileForm1(instance = request.user)
        
    context = {'form':form}
    return render(request, 'TTU_SYSTEM/edit_profile1.html',context)

def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/TTU_SYSTEM/profile')

        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user = request.user)

    context = {'form':form}
    return render(request,'TTU_SYSTEM/change_password.html',context)