from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('full_name', 'username', 'email', 'password')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()