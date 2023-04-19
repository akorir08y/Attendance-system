from django import forms
from TTU_SYSTEM.models import CustomUser,LecProfile,UserProfile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import transaction
from django.forms import ModelForm
from django.utils import timezone
import pytz

class LecRegForm(UserCreationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Password'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','password1','password2','email')

    @transaction.atomic
    def save(self, commit=True):
        user = super(LecRegForm,self).save(commit=False)
        if commit:
            user.save()
        return user

class LecProfileForm(ModelForm):
    Employee_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Employee'}))
    Department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Department'}))
    Unit = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Unit'}))
    lec_image = forms.FileField()

    class Meta:
        model = LecProfile
        fields = ( 'role' ,'Employee_no','Department','Unit','lec_image')

    @transaction.atomic
    def save(self, commit=True):
        user = super(LecProfileForm,self).save(commit=False)
        if commit:
            user.save()
        return user

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = LecProfile
        fields = ( 'role' ,'Employee_no','Department','Unit','lec_image')


class StdRegForm(UserCreationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Password'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','password1','password2','email')

    @transaction.atomic
    def save(self, commit=True):
        user = super(StdRegForm,self).save(commit=False)
        if commit:
            user.save()
        return user

class UserProfileForm(ModelForm):
    reg_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Reg_No'}))
    year = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Department'}))
    course = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Course'}))
    your_image = forms.FileField()

    class Meta:
        model = UserProfile
        fields = ('role' ,'reg_no','year','course','your_image')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserProfileForm,self).save(commit=False)
        if commit:
            user.save()
        return user

class EditProfileForm1(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ( 'role' ,'reg_no','year','course','your_image')


