from django import forms

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='nombre')
    message = forms.CharField(label='Mensaje')