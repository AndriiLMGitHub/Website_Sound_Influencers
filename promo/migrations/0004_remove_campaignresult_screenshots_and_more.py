# Generated by Django 4.2.4 on 2023-08-21 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0003_alter_promo_date_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaignresult',
            name='screenshots',
        ),
        migrations.CreateModel(
            name='CampaignResultScreenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshots', models.FileField(upload_to='screenshoots/')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaign_images', to='promo.campaignresult')),
            ],
        ),
    ]
