# Generated by Django 3.2.25 on 2024-07-04 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20240704_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='agent_assign',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
