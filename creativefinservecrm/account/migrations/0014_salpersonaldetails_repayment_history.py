# Generated by Django 3.1.7 on 2022-01-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20220122_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='salpersonaldetails',
            name='repayment_history',
            field=models.CharField(choices=[(None, '-- Good or Bad --'),('Good', 'Good'),('Bad', 'Bad')], default=None, max_length=4),
        )
    ]
