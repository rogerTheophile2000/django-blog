# Generated by Django 4.2.1 on 2023-07-17 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_article_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='coonclusion',
            new_name='conclusion',
        ),
        migrations.AddField(
            model_name='article',
            name='conclusiontile',
            field=models.CharField(default=datetime.datetime(2023, 7, 17, 2, 42, 42, 343470, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
    ]
