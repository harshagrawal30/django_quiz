# Generated by Django 3.1.2 on 2020-11-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20201122_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='que',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
