# Generated by Django 3.2.5 on 2022-01-20 12:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 12, 41, 21, 227323, tzinfo=utc), verbose_name='date published'),
        ),
    ]
