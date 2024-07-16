from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Flan, ContactForm
# from .forms import ContactFormForm
from .forms import ContactFormModelForm

# Create your views here.

from .models import Flan

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def base1(request):
    return render(request, 'base.html', {})

def success(request):
    return render(request, 'exito.html', {})

# def contacto(request):
#     if request.method == 'POST':
#         form = ContactFormForm(request.POST)
#         if form.is_valid():
#             contact_form = ContactForm.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect('/exito')
#     else:
#         form = ContactFormForm()   
#     return render(request, 'contacto.html',{'form':form})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()   
    return render(request, 'contacto.html',{'form':form})

def salir(request):
    logout(request)
    return redirect('/')