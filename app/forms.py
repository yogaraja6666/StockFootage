from django import forms
from .models import Post, User, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ImageUploadForm(forms.ModelForm):
    orientation = forms.ChoiceField(choices=[('portrait', 'Portrait'), ('landscape', 'Landscape'), ('square', 'Square')],
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = ['image','orientation','title', 'tag','location'] 
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class CustomUserForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2', 'profile_picture']


'''
class EditUserProfileForm(UserChangeForm):
    password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name','profile_picture']        
'''

class UserupdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name',]

class ProfileupdateForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['image']
                