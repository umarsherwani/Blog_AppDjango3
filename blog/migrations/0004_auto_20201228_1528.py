# Generated by Django 3.1.4 on 2020-12-28 23:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201225_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
