import pdb
from unicodedata import name
from urllib import response
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreateContact, CreateOpportunity, ContactForm, OpportunityForm
from .models import Contacts, Opportunity
from django.db.models import Q
from django.forms.models import model_to_dict
# Create your views here.

# Home page
def dashboard(request):
	contacts = Contacts.objects.all()
	opportunity = Opportunity.objects.all()
	total_contacts = contacts.count()
	context = {'contacts':contacts, 'opportunity':opportunity,
	           'total_contacts':total_contacts }
	return render(request, 'sales_force.html', context)

###### Create views ######
def create_contact(response):
    if response.method == 'POST':
        form = CreateContact(response.POST, response.FILES)
        if form.is_valid():
            # file_attached = form.cleaned_data['attachments']
            # # pdb.set_trace()
            # if file_attached.size > MAX_FILE_SIZE:
            #     raise forms.ValidationError("keep upload size below 1mb")
            new_contact = Contacts(
                name = form.cleaned_data['name'],
                account = form.cleaned_data['account'],
                address = form.cleaned_data['address'],
                title = form.cleaned_data['title'],
                work_phone = form.cleaned_data['work_phone'],
                mobile_phone = form.cleaned_data['mobile_phone'],
                email = form.cleaned_data['email'],
                attachments = form.cleaned_data['attachments'],
            )
            new_contact.save()
            
    else:
        form = CreateContact()
    return render(response, 'create_contact.html', {"form": form})

def create_opportunity(response):
    if response.method == 'POST':
        form = CreateOpportunity(response.POST)
        if form.is_valid():
            primary_contact_id = form.cleaned_data['primary_contact']
            primary_contact = Contacts.objects.get(pk = int(primary_contact_id))
            new_opportunity = Opportunity(
                name = form.cleaned_data['name'],
                win_percentage = form.cleaned_data['win_percentage'],
                account = form.cleaned_data['account'],
                primary_contact = primary_contact,
                close_date = form.cleaned_data['close_date'],
                estimated_revenue = form.cleaned_data['estimated_revenue'],
                risk_level = form.cleaned_data['risk_level'],
            )
            new_opportunity.save()
            for contact_selected in form.cleaned_data['contacts']:
                new_opportunity.contacts.add(contact_selected)
    else:
        form = CreateOpportunity()
    return render(response, 'create_opportunity.html', {"form": form})


###### Display views ######
def get_contact(response, contact_id):
    contact = Contacts.objects.get(pk = int(contact_id))
    form = ContactForm(instance = contact)
    return render(response, 'edit_contact.html', {"form": form, "id": contact_id, "file_url": contact.attachments.url})

def get_opportunity(response, opportunity_id):
    opportunity = Opportunity.objects.get(pk = int(opportunity_id))
    form = OpportunityForm(instance = opportunity)
    return render(response, 'edit_opportunity.html', {"form": form, "id": opportunity_id})

###### Search views ######
def search_contacts(response):
    query = response.GET.get('q')
    context = {"contacts": Contacts.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))}
    return render(response, 'search_contacts.html', context)

def search_opportunities(response):
    query = response.GET.get('q')
    context = {"opportunity": Opportunity.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))}
    return render(response, 'search_opportunity.html', context)

###### List views ######
def contacts(response):
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render(response, 'contacts.html', context)

def opportunities(response):
    opportunities = Opportunity.objects.all()
    context = {'opportunities': opportunities}
    return render(response, 'opportunities.html', context)


###### Update views ###### 
def update_contact(response, contact_id): 
    contact_to_update = Contacts.objects.get(pk=int(contact_id))
    form = CreateContact(response.POST, response.FILES)
    if form.is_valid():
        contact_to_update.name = form.cleaned_data['name']
        contact_to_update.account = form.cleaned_data['account']
        contact_to_update.address = form.cleaned_data['address']
        contact_to_update.title = form.cleaned_data['title']
        contact_to_update.work_phone = form.cleaned_data['work_phone']
        contact_to_update.mobile_phone = form.cleaned_data['mobile_phone']
        contact_to_update.email = form.cleaned_data['email']
        contact_to_update.attachments = form.cleaned_data['attachments']
        contact_to_update.save()
    return redirect(f"salesforce")

def update_opportunity(response, opportunity_id):
    opportunity_to_update = Opportunity.objects.get(pk=int(opportunity_id))
    form = CreateOpportunity(response.POST)
    if form.is_valid():
        primary_contact_id = form.cleaned_data['primary_contact']
        primary_contact = Contacts.objects.get(pk = int(primary_contact_id))
        opportunity_to_update.name = form.cleaned_data['name']
        opportunity_to_update.win_percentage = form.cleaned_data['win_percentage']
        opportunity_to_update.account = form.cleaned_data['account']
        opportunity_to_update.primary_contact = primary_contact
        opportunity_to_update.close_date = form.cleaned_data['close_date']
        opportunity_to_update.estimated_revenue = form.cleaned_data['estimated_revenue']
        opportunity_to_update.risk_level = form.cleaned_data['risk_level']
        opportunity_to_update.contacts.clear()
        opportunity_to_update.save()
        pdb.set_trace()
        for contact_selected in form.cleaned_data['contacts']:
            opportunity_to_update.contacts.add(contact_selected)
    return redirect(f"salesforce")

###### Deletion views ###### 
def delete_contact(response, contact_id):
    Contacts.objects.get(pk = int(contact_id)).delete()
    return redirect('salesforce')

def delete_opportunity(response, opportunity_id):
    Contacts.objects.get(pk = int(opportunity_id)).delete()
    return redirect('salesforce')


