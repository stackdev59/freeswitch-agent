# Generated by Django 5.0.7 on 2024-07-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0009_agent_created_at_agent_policies_agent_rules_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='methodType',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
