# Generated by Django 5.0.7 on 2024-07-17 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_created_date_post_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='marked',
            field=models.BooleanField(default=False, null=True, verbose_name='즐겨찾기'),
        ),
    ]
