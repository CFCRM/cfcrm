# Generated by Django 3.1.7 on 2021-08-13 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='status',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='type_of_partner',
        ),
    ]
