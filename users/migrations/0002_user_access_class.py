# Generated by Django 4.2.6 on 2025-02-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_class',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
