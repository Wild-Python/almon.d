from django import forms
from .models import Almon


class AlmonForm(forms.ModelForm):
    class Meta:
        model = Almon
        # fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AlmonForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Email'}
        )
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        self.fields['application_type'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'e.g., Website, Mobile App, Desktop Application'})
        self.fields['application_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'e.g., Google, WhatsApp, PyCharm'})
