# Generated by Django 3.1.2 on 2020-11-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account3', '0004_user_res_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_res',
            name='biology',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_res',
            name='chemistry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_res',
            name='maths',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_res',
            name='physics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_res',
            name='science',
            field=models.BooleanField(default=False),
        ),
    ]
