# Generated by Django 3.2.12 on 2023-09-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seating_arranger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classcsv',
            name='name',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]