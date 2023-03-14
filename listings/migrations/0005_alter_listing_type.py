# Generated by Django 4.1.6 on 2023-03-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_category_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('R', 'For Rent'), ('S', 'For Sale'), ('L', 'For Lease')], max_length=1),
        ),
    ]
