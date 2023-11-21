from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label=' confirma contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}
        def __init__(self, *args, **kwargs):
            super(UserRegistrationForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['class'] = 'form-control col-md-6'
            #self.fields['email'].widget.attrs.update({'my_attribute_key':'my_attribute_value'})


