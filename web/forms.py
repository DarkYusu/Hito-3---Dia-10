from django import forms
from django.forms import ModelForm
from web.models import ContactForm

# class ContactFormForm(forms.Form):
#     customer_email = forms.EmailField(label='Correo')
#     customer_name = forms.CharField(max_length=64, label='nombre')
#     message = forms.CharField(label='Mensaje')


class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }