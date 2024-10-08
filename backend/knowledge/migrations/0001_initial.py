# Generated by Django 3.2.25 on 2024-07-04 03:08

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('raw', models.TextField()),
                ('file', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ubuntu/nexvoz/epic-dashboard/media'), upload_to='knowledge_uploads/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='knowledge', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
