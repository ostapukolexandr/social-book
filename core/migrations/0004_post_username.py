# Generated by Django 4.2.5 on 2023-09-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_alter_profile_profileing'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
