# Generated by Django 3.1.7 on 2021-12-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210813_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='alt_phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='leads',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='leads',
            name='loan_amt',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='leads',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='leads',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='leads',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
