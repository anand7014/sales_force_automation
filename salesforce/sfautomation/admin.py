from django.contrib import admin

# Register your models here.
from .models import Contacts, Opportunity


admin.site.register(Contacts)
admin.site.register(Opportunity)
