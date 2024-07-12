from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_private')
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(ContactForm)