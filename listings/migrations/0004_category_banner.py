# Generated by Django 4.1.6 on 2023-03-13 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banner_imgs/'),
        ),
    ]