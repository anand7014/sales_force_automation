from django import forms
from .models import RISK_LEVELS, Contacts, Opportunity

class CreateContact(forms.Form):
    name = forms.CharField(label= "Name", max_length=200)
    account = forms.CharField(label= "Account", max_length=200)
    address = forms.CharField(label= "Address", max_length=200)
    title = forms.CharField(label= "Title", max_length=200)
    work_phone = forms.CharField(label= "Work Phone", max_length=10)
    mobile_phone = forms.CharField(label= "Mobile Phone", max_length=10)
    email = forms.EmailField(label= "Email", max_length=200)
    attachments = forms.FileField(label= "Attach file")


class CreateOpportunity(forms.Form):
    name = forms.CharField(max_length=200)
    win_percentage = forms.CharField(max_length=2)
    account = forms.CharField(max_length=200)
    primary_contact = forms.ChoiceField(choices=[(x.contacts_id,x.name) for x in Contacts.objects.all()])
    close_date = forms.DateTimeField()
    estimated_revenue = forms.CharField(max_length=200)
    risk_level = forms.ChoiceField(choices = RISK_LEVELS)
    contacts = forms.ModelMultipleChoiceField(queryset = Contacts.objects.all(), widget=forms.CheckboxSelectMultiple)