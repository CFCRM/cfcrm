# Generated by Django 3.1.7 on 2022-01-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_salpersonaldetails_repayment_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salpersonaldetails',
            name='repayment_history',
            field=models.CharField(blank=True, choices=[(None, '-- Good or Bad --'), ('Good', 'Good'), ('Bad', 'Bad')], default=None, max_length=4, null=True),
        ),
    ]
