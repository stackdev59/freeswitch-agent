# Generated by Django 3.2.25 on 2024-07-02 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0004_agent_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='interruption',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='temperature',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
