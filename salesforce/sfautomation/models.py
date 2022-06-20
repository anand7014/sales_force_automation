from random import choices
from django.conf import settings
from django.db import models

RISK_LEVELS = (
    ('HIGH', 'HIGH'), 
    ('LOW', 'LOW'), 
    ('MEDIUM', 'MEDIUM')
)
class Contacts(models.Model):
    contacts_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    work_phone = models.CharField(max_length=10)
    mobile_phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    attachments = models.FileField(upload_to='media/attachments', default='', null=True, blank=True)
    class Meta:
        ordering = ['contacts_id']
     
    def __str__(self):
        return f"{self.contacts_id}"

class Opportunity(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    win_percentage = models.CharField(max_length=2)
    account = models.CharField(max_length=200)
    primary_contact = models.ForeignKey(Contacts, null=True, on_delete=models.CASCADE)
    close_date = models.DateTimeField(null=True, blank=True)
    estimated_revenue = models.CharField(max_length=200)
    risk_level = models.CharField(max_length=6, choices = RISK_LEVELS, default='LOW')
    contacts = models.ManyToManyField(Contacts, related_name='opportunitys', null=True, blank=True)

    class Meta:
        ordering = ['opportunity_id']
     
    def __str__(self):
        return f"{self.opportunity_id}"

