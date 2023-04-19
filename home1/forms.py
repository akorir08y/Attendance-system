from django import forms
from home1.models import Post
from django.db import transaction

class HomeForm1(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    comment = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}))
    
    class Meta:
        model = Post
        fields = ('title','comment')

