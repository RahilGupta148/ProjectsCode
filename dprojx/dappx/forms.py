from django import forms
from django.contrib.auth.models import User
from dappx.models import UserProfileInfo,Document

class DocumentForm(forms.ModelForm):
    class Meta():
        model=Document
        fields=('description','vidimage','project_video','docname',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    contact = forms.IntegerField()
    class Meta():
        model = User
        fields = ('username','email','password','contact')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields =('portfolio_site','profile_pic')
