# Generated by Django 3.1.2 on 2021-05-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='OCRtext',
            field=models.CharField(default='No text extracted', max_length=500),
        ),
    ]