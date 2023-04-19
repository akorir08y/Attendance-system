from django.shortcuts import render,redirect
from TTU_SYSTEM.forms import (LecRegForm,EditProfileForm,LecProfileForm)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from ..decorators import lecturer_required
from TTU_SYSTEM.models import CustomUser


def home(request):
    return render(request,'home/home.html')


def lec_gallery(request):
    return render(request,'TTU_SYSTEM/lec_gallery.html')


def lec_register(request):
    if request.method =='POST':
        form = LecRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TTU_SYSTEM:login_success')

    else:
        form = LecRegForm()

    context = {'form':form}
    return render(request, 'TTU_SYSTEM/LecReg.html',context)



def lec_profileform(request):
    if request.method =='POST':
        form = LecProfileForm(request.POST)
        if form.is_multipart(request.POST,request.FILES):
            form.save()
            return redirect ('home')
    else:
        form = LecProfileForm()

    context = {'form':form}
    return render(request,'TTU_SYSTEM/lec_profileform.html',context)

def lec_profile(request,id=None):
    if id:
        user = CustomUser.objects.get(id=id)
    else:
        user = request.user
    context = {'user':request.user}
    return render(request, 'TTU_SYSTEM/lec_profile.html',context)

def lec_profile_with_pk(request,id=None):
    if id:
        user = CustomUser.objects.get(id=id)
    else:
        user = request.user
    context = {'user':request.user}
    return render(request, 'TTU_SYSTEM/lec_profile_with_pk.html',context)

def lec_edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('lec_profile')
    else:
        form = EditProfileForm(instance = request.user)
        
    context = {'form':form}
    return render(request, 'TTU_SYSTEM/edit_profile.html',context)

def lec_change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/TTU_SYSTEM/lec_profile')

        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user = request.user)

    context = {'form':form}
    return render(request,'TTU_SYSTEM/lec_change_password.html',context)