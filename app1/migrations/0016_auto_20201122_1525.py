# Generated by Django 3.1.2 on 2020-11-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_que_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='que',
            name='pub_date',
            field=models.DateTimeField(default=2008, verbose_name='date published'),
        ),
    ]
