# Generated by Django 4.2.4 on 2023-08-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_email_verify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_verify',
        ),
        migrations.AddField(
            model_name='user',
            name='verification_key',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ключ верификации'),
        ),
    ]
