from django import forms
from django.contrib.auth.models import User


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')

        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(['Email already exists, please try another one.'])
        if User.objects.filter(username=username_value).exists():
            self._errors['username'] = self.error_class(['Username already exists, please try another one.'])

        return field_data



