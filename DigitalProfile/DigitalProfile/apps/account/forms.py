from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


from .models import Account
from profile.models import Profile

class AuthForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = Account 
        fields = ('password',)       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
    

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email','password1', 'password2','vk_id')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
    

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'skills','avatar')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
    