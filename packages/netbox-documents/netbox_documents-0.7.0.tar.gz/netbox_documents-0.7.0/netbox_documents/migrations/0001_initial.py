# Generated by Django 4.0.3 on 2022-04-04 19:31

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import netbox_documents.utils
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0153_created_datetimefield'),
        ('circuits', '0034_created_datetimefield'),
        ('extras', '0072_created_datetimefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('document', models.FileField(upload_to=netbox_documents.utils.file_upload)),
                ('document_type', models.CharField(max_length=30)),
                ('comments', models.TextField(blank=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='dcim.site')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('-created', 'name'),
            },
        ),
        migrations.CreateModel(
            name='DeviceDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('document', models.FileField(upload_to=netbox_documents.utils.file_upload)),
                ('document_type', models.CharField(max_length=30)),
                ('comments', models.TextField(blank=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CircuitDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('document', models.FileField(upload_to=netbox_documents.utils.file_upload)),
                ('document_type', models.CharField(max_length=30)),
                ('comments', models.TextField(blank=True)),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='circuits.circuit')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
