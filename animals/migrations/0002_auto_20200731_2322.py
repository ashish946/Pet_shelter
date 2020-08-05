# Generated by Django 3.0.8 on 2020-07-31 17:52

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='Sheltered',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='animal',
            name='age',
            field=models.CharField(choices=[('Young', 'YOUNG'), ('Old', 'OLD')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal',
            field=models.CharField(choices=[('Cat', 'CAT'), ('Dog', 'DOG')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='description',
            field=models.TextField(max_length=360, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='difficulty',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)]),
        ),
        migrations.AddField(
            model_name='animal',
            name='gender',
            field=models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]