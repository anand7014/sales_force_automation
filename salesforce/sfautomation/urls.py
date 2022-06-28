from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('salesforce', views.dashboard, name='salesforce'),
    # create apis
    path('salesforce/create_contact', views.create_contact, name='create_contact'),
    path('salesforce/create_opportunity', views.create_opportunity, name='create_opportunity'),
    # search apis
    path('salesforce/search_opportunity', views.search_opportunities),
    path('salesforce/search_contact', views.search_contacts),
    # get one instance
    path('salesforce/contact/<int:contact_id>', views.get_contact, name='show_contact'),
    path('salesforce/opportunity/<int:opportunity_id>', views.get_opportunity, name='show_opportunity'),

    # get all instances
    path('salesforce/contacts', views.contacts, name='contacts'),
    path('salesforce/opportunities', views.opportunities, name='opportunities'),

    #delete
    path('salesforce/contact/<int:contact_id>/delete', views.delete_contact, name='delete_contact'),
    path('salesforce/opportunity/<int:opportunity_id>/delete', views.delete_opportunity, name='delete_opportunity'),

    #update
    path('salesforce/contact/<int:contact_id>/edit', views.update_contact, name='update_contact'),
    path('salesforce/opportunity/<int:opportunity_id>/edit', views.update_opportunity, name='update_opportunity'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)