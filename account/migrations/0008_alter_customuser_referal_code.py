# Generated by Django 4.2.4 on 2023-08-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='referal_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
