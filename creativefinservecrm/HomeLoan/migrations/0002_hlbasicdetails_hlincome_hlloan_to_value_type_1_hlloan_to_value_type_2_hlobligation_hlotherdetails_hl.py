# Generated by Django 3.1.7 on 2022-01-26 12:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_productsorservices'),
        ('HomeLoan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HlBasicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(max_length=50)),
                ('minimum_age', models.IntegerField()),
                ('retirement_age', models.IntegerField()),
                ('maximum_age_consider_govt', models.IntegerField()),
                ('maximum_age_consider_others', models.IntegerField()),
                ('minimum_loan_amount', models.FloatField()),
                ('maximum_loan_amount', models.FloatField()),
                ('total_experience', models.IntegerField()),
                ('company_profitability', models.BooleanField()),
                ('form_16', models.BooleanField()),
                ('profession_tax_deduction', models.BooleanField()),
                ('negative_employer_profile', models.BooleanField()),
                ('company_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.companytype')),
                ('customer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.customertype')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.designationtype')),
                ('salary_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.salarytype')),
            ],
        ),
        migrations.CreateModel(
            name='HlProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('builder_category', models.BooleanField()),
                ('apf', models.BooleanField()),
                ('occupation_certificate', models.BooleanField()),
                ('cc_municipal_plan_tax_receipt', models.BooleanField()),
                ('previous_aggrement_available', models.BooleanField()),
                ('subvention_scheme', models.BooleanField()),
                ('percent_of_completion', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('property_age', models.IntegerField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('negative_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.negativearea')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.propertytype')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.roomtype')),
                ('stage_of_construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.stageofconstruction')),
            ],
        ),
        migrations.CreateModel(
            name='HlOtherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_of_interest', models.IntegerField()),
                ('prevailing_rate', models.IntegerField()),
                ('tenure', models.IntegerField()),
                ('inward_cheque_return', models.BooleanField()),
                ('multiple_inquiry', models.BooleanField()),
                ('relation_eligible', models.CharField(max_length=25)),
                ('relation_not_eligible', models.CharField(max_length=25)),
                ('basic_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
            ],
        ),
        migrations.CreateModel(
            name='HlObligation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emi_obligation', models.BooleanField()),
                ('emi_obligation_not_consider', models.IntegerField()),
                ('credit_card', models.BooleanField()),
                ('credit_card_obligation_percent', models.IntegerField()),
                ('gold_loan', models.BooleanField()),
                ('gold_loan_percent', models.IntegerField()),
                ('basic_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
            ],
        ),
        migrations.CreateModel(
            name='HlLoan_To_Value_Type_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_age', models.IntegerField()),
                ('ltv_percent_for_fresh', models.IntegerField()),
                ('ltv_percent_for_balance_transfer', models.IntegerField()),
                ('tenure_percent_for_fresh', models.IntegerField()),
                ('tenure_percent_for_balance_transfer', models.IntegerField()),
                ('basic_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
            ],
        ),
        migrations.CreateModel(
            name='HlLoan_To_Value_Type_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rbi_guidelines', models.IntegerField()),
                ('amenity', models.IntegerField()),
                ('car_parking', models.BooleanField()),
                ('car_parking_amount', models.IntegerField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('loan_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.loanamount')),
            ],
        ),
        migrations.CreateModel(
            name='HlIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_salary', models.BooleanField(default=None)),
                ('net_salary', models.BooleanField(default=None)),
                ('bonus', models.BooleanField(default=None)),
                ('bonus_avg_yearly', models.IntegerField()),
                ('bonus_avg_yearly_percentage', models.IntegerField()),
                ('income_foir_yearly', models.BooleanField(default=None)),
                ('bonus_avg_quarter', models.IntegerField()),
                ('bonus_avg_quarter_percentage', models.IntegerField()),
                ('income_foir_quarter', models.BooleanField(default=None)),
                ('bonus_avg_half_yearly', models.IntegerField()),
                ('bonus_avg_half_yearly_percentage', models.IntegerField()),
                ('income_foir_half_yearly', models.BooleanField(default=None)),
                ('rent_income', models.BooleanField(default=None)),
                ('rent_agreement_type', models.CharField(max_length=25)),
                ('bank_reflection', models.BooleanField(default=None)),
                ('rent_reflection_in_bank', models.IntegerField()),
                ('rent_income_percentage', models.IntegerField()),
                ('co_applicant_no_income_only_rent_income', models.BooleanField(default=None)),
                ('co_applicant_mandatory', models.BooleanField(default=None)),
                ('future_rent', models.BooleanField(default=None)),
                ('future_rent_percentage', models.IntegerField()),
                ('income_foir_future_rent', models.IntegerField()),
                ('incentive', models.BooleanField(default=None)),
                ('incentive_avg_months', models.IntegerField()),
                ('income_foir_incentive', models.BooleanField(default=None)),
                ('income_foir', models.IntegerField()),
                ('basic_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
            ],
        ),
    ]
