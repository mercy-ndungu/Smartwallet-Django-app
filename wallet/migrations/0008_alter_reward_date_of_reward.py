# Generated by Django 4.1 on 2022-09-01 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_alter_thirdparty_date_of_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='date_of_reward',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]