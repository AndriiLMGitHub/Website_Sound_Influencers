# Generated by Django 4.2.4 on 2023-08-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]