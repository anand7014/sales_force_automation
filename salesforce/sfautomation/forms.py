from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import RISK_LEVELS, Contacts, Opportunity

MAX_FILE_SIZE = 1000000

class CreateContact(forms.Form):
    name = forms.CharField(label= "Name", max_length=200)
    account = forms.CharField(label= "Account", max_length=200)
    address = forms.CharField(label= "Address", max_length=200, widget=forms.Textarea)
    title = forms.CharField(label= "Title", max_length=200)
    work_phone = forms.CharField(label= "Work Phone", max_length=10)
    mobile_phone = forms.CharField(label= "Mobile Phone", max_length=10)
    email = forms.EmailField(label= "Email", max_length=200)
    attachments = forms.FileField(label= "Attach file",required=False)
    def clean_attachments(self):
        file_attached = self.cleaned_data['attachments']
        if file_attached.size > MAX_FILE_SIZE:
            raise forms.ValidationError("keep upload size below 1mb")
        return file_attached


class CreateOpportunity(forms.Form):
    name = forms.CharField(max_length=200)
    win_percentage = forms.CharField(max_length=2)
    account = forms.CharField(max_length=200)
    close_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    estimated_revenue = forms.CharField(max_length=200)
    risk_level = forms.ChoiceField(choices = RISK_LEVELS)
    contacts = forms.ModelMultipleChoiceField(queryset = Contacts.objects.all(), widget=forms.CheckboxSelectMultiple)
    primary_contact = forms.ChoiceField(choices=[(x.contacts_id,x.name) for x in Contacts.objects.all()])

class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'


class OpportunityForm(ModelForm):
    class Meta:
        model = Opportunity
        fields = '__all__'