# Generated by Django 3.1.2 on 2020-11-22 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20201122_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='que',
            name='biology',
        ),
        migrations.RemoveField(
            model_name='que',
            name='chemistry',
        ),
        migrations.RemoveField(
            model_name='que',
            name='physics',
        ),
        migrations.RemoveField(
            model_name='que',
            name='science',
        ),
    ]
