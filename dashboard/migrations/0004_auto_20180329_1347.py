# Generated by Django 2.0.3 on 2018-03-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180329_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='Location',
        ),
        migrations.AddField(
            model_name='signup',
            name='Location',
            field=models.TextField(null=True),
        ),
    ]