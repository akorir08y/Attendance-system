from attendance.models import UserGroup,Post2
from django.db import transaction
from django.contrib.auth.forms import forms



class CreateGroup(forms.ModelForm):


    class Meta:
        model = UserGroup
        fields = ('users','group')
   
    @transaction.atomic
    def save(self, commit=True):
        user = super(UserGroup,self).save(commit=False)
        if commit:
            user.save()
        return user

class HomeForm2(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    comment = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}))
    
    class Meta:
        model = Post2
        fields = ('title','comment')