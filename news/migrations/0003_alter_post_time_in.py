# Generated by Django 4.2 on 2023-06-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
