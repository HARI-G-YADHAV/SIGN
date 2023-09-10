# Generated by Django 3.2.12 on 2023-09-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedcsv',
            name='file',
        ),
        migrations.RemoveField(
            model_name='uploadedcsv',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='uploadedcsv',
            name='RegNo',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadedcsv',
            name='status',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
