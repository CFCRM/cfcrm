# Generated by Django 3.1.7 on 2022-01-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220118_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='details_about_default',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
