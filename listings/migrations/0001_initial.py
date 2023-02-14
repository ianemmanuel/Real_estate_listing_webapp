# Generated by Django 4.1.6 on 2023-02-13 11:52

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cat_imgs/')),
            ],
            options={
                'verbose_name_plural': '2. Categories',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pub_imgs/')),
            ],
            options={
                'verbose_name_plural': '3.Publishers',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('square_footage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('slug', models.CharField(default=models.CharField(max_length=200), max_length=400)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded/')),
                ('detail', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('payment_type', models.CharField(choices=[(1, 'Rent'), (2, 'For Sale')], default=(1, 'Rent'), max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('is_featured', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.location')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
