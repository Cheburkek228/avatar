from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label='Ваш ник')
    password = forms.CharField(label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__password'
            }
        )
    )
    def clean_username(self):
        profile = self.cleaned_data.get('username')
        queryset = User.objects.filter(username__iexact=profile)
        
        if not queryset.exists():
            raise forms.ValidationError("This username or password does not exists")
        return profile      

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__password'
            }
        )
    )
    def clean_username(self):
        profile = self.cleaned_data.get('username')
        queryset = User.objects.filter(username__iexact=profile)

        if queryset.exists():
            raise forms.ValidationError("This username is already taken")    
        return profile

    