# Generated by Django 5.0.7 on 2024-07-25 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_role_manage_id_userprofile_role_manage'),
        ('roles', '0002_auto_20240723_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role_manage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='roles.group'),
        ),
    ]
