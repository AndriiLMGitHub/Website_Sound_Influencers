# Generated by Django 4.2.4 on 2023-08-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
