# Generated by Django 3.1.2 on 2020-11-23 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_auto_20201122_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='que',
            name='end_date',
            field=models.DateTimeField(default=None, verbose_name='Date Expired'),
        ),
    ]