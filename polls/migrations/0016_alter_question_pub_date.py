# Generated by Django 3.2.5 on 2022-02-08 20:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 20, 21, 52, 635903, tzinfo=utc), verbose_name='date published'),
        ),
    ]
