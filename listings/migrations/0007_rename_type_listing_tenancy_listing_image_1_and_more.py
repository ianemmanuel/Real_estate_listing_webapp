# Generated by Django 4.1.6 on 2023-03-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_delete_banner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='type',
            new_name='tenancy',
        ),
        migrations.AddField(
            model_name='listing',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='image_imgs1/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='image_imgs2/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='image_imgs3/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='image_imgs4/'),
        ),
    ]
