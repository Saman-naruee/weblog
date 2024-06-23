# Generated by Django 5.0.1 on 2024-05-02 16:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Description', models.TextField()),
                ('Slug', models.SlugField(max_length=250)),
                ('Publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published'), ('RJ', 'Rejected')], default='DF', max_length=2)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Publish'],
                'indexes': [models.Index(fields=['-Publish'], name='publish_idx')],
            },
        ),
    ]
