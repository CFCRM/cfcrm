# Generated by Django 3.1.7 on 2022-01-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_lessetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencetype',
            name='residence_type',
            field=models.CharField(max_length=30),
        ),
    ]
