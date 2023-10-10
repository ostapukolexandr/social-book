# Generated by Django 4.2.5 on 2023-09-17 17:00

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_profileing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('caption', models.TextField()),
                ('number_of_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileing',
            field=models.ImageField(default='logo2.png', upload_to='profile_images'),
        ),
    ]
