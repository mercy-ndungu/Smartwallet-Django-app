# Generated by Django 4.1 on 2022-09-01 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_currency_notification_thirdparty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date_of_issue',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
