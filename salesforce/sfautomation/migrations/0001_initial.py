# Generated by Django 4.0.5 on 2022-06-19 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('contacts_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('work_phone', models.CharField(max_length=10)),
                ('mobile_phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
                ('attachments', models.FileField(blank=True, default='', null=True, upload_to='media/attachments')),
            ],
            options={
                'ordering': ['contacts_id'],
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('opportunity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('win_percentage', models.CharField(max_length=2)),
                ('account', models.CharField(max_length=200)),
                ('close_date', models.DateTimeField(blank=True, null=True)),
                ('estimated_revenue', models.CharField(max_length=200)),
                ('risk_level', models.CharField(choices=[('HIGH', 'HIGH'), ('LOW', 'LOW'), ('MEDIUM', 'MEDIUM')], default='LOW', max_length=6)),
                ('contacts', models.ManyToManyField(blank=True, null=True, related_name='opportunitys', to='sfautomation.contacts')),
                ('primary_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sfautomation.contacts')),
            ],
            options={
                'ordering': ['opportunity_id'],
            },
        ),
    ]