# Generated by Django 3.1.7 on 2022-01-19 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20220119_1107'),
        ('account', '0006_salresidencedetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salexistingloandetails',
            old_name='add_det_id',
            new_name='addi_details_id',
        ),
        migrations.RemoveField(
            model_name='salexistingloandetails',
            name='application_type',
        ),
        migrations.RemoveField(
            model_name='salexistingloandetails',
            name='outstan_paid_by_customer',
        ),
        migrations.AddField(
            model_name='salexistingloandetails',
            name='applicant_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='master.applicanttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salexistingloandetails',
            name='outstanding_amount_paid_by_customer',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='any_bounces',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='bank_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.bankname'),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='emi',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='emi_start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='loan_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='moratorium_taken',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='outstanding_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.product'),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='rate_of_interest',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='salexistingloandetails',
            name='tenure',
            field=models.IntegerField(),
        ),
    ]
