# Generated by Django 3.1.2 on 2020-11-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account3', '0002_user_res_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_res',
            name='solved_c_n',
            field=models.BooleanField(default=False),
        ),
    ]
