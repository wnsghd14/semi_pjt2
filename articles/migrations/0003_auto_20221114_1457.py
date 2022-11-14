# Generated by Django 3.2.13 on 2022-11-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='x',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='y',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
