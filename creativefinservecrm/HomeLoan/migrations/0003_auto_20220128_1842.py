# Generated by Django 3.1.7 on 2022-01-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeLoan', '0002_hlbasicdetails_hlincome_hlloan_to_value_type_1_hlloan_to_value_type_2_hlobligation_hlotherdetails_hl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hlincome',
            name='bank_reflection',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='bonus',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='co_applicant_mandatory',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='co_applicant_no_income_only_rent_income',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='future_rent',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='gross_salary',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='incentive',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='income_foir_half_yearly',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='income_foir_incentive',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='income_foir_quarter',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='income_foir_yearly',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='net_salary',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='hlincome',
            name='rent_income',
            field=models.BooleanField(),
        ),
    ]
