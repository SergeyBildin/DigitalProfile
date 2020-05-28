from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account
from profile.models import Profile

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
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
    