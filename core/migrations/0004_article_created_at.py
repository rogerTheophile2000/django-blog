# Generated by Django 4.2.1 on 2023-07-17 02:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_coonclusion_article_conclusion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 7, 17, 2, 46, 30, 537804, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]