# Generated by Django 3.1.2 on 2020-11-22 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20201122_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='que',
            name='biology',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='que',
            name='chemistry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='que',
            name='physics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='que',
            name='science',
            field=models.BooleanField(default=False),
        ),
    ]
