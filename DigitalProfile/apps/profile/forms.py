from django import forms
from .models import Profile



class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'avatar', 'skills', 'skill_groups')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

class AvatarUpload(forms.ModelForm):
    avatar = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'ask-signup-avatar-input',}),
        required=False, label=u'Аватар')

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar is None:
            raise forms.ValidationError(u'Добавьте картинку')
        if 'image' not in avatar.content_type:
            raise forms.ValidationError(u'Неверный формат картинки')
        return avatar
    
    class Meta:
        model = Profile
        fields = ('avatar',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

