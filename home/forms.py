from django import forms
from home.models import Post1

class HomeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    comment = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}))

    class Meta:
        model = Post1
        fields = ('title','comment')