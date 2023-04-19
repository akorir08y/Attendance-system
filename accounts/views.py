from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def gallery(request):
    return render(request,'accounts/gallery.html')

def register(request):
    if request.method =='POST':
        form = StdRegForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    else:
        form = StdRegForm()

    context = {'form':form}
    return render(request, 'accounts/StdReg.html',context)

def view_profile(request):
    context = {'user':request.user}
    return render(request, 'accounts/profile.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('view_profile','lec_profile')
    else:
        form = EditProfileForm(instance = request.user)
        
    context = {'form':form}
    return render(request, 'accounts/edit_profile.html',context)


