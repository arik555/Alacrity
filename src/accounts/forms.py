from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)

User = get_user_model()

class MyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("User does not exist.")
        if not user.check_password(password):
            raise ValidationError("Incorrect Username or Password.")
        if not user.is_active:
            raise ValidationError("User is not active.")
        return super(MyLoginForm, self).clean(*args, **kwargs)


class MyRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
        ]

