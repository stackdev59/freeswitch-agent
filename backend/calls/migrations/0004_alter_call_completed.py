# Generated by Django 3.2.25 on 2024-06-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0003_alter_call_agent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
