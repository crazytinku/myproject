from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomLoginForm(AuthenticationForm):
    def clean_username(self):
        """Ensure only emails from @nttf.co.in domain are allowed."""
        email = self.cleaned_data.get('username')
        if email and not email.endswith('@nttf.co.in'):
            raise forms.ValidationError("Only @nttf.co.in emails are allowed.")
        return email
    
    def clean(self):
        """Validate credentials and ensure user exists."""
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid credentials, please try again.")
        
        return cleaned_data
