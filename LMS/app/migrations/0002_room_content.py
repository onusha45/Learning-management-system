# Generated by Django 5.0.7 on 2024-07-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='content',
            field=models.TextField(max_length=200, null=True),
        ),
    ]