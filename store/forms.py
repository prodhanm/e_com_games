from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password1', 'password2')

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    name = forms.CharField(max_length=50, required=True)
    from_email = forms.EmailField(max_length=50, required=True)
    message = forms.CharField(
        max_length=2000,
        required=True, 
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )