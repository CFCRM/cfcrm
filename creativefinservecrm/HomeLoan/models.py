from django.db import models
from django.conf import settings
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from master.models import CompanyType, CustomerType, DesignationType, Product, SalaryType
from django.core.validators import MaxValueValidator, MinValueValidator


class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=25)
    cust_type = models.CharField(max_length=25)


class Age(models.Model):
    age_id = models.AutoField(primary_key=True)
    min_age = models.IntegerField()
    retire_age = models.IntegerField()
    max_age_consi_others = models.IntegerField()
    max_age_consi_gov = models.IntegerField()
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class Cibil(models.Model):
    cibil_id = models.AutoField(primary_key=True)
    cibil_range_min = models.IntegerField()
    cibil_range_max = models.IntegerField()
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class Company(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_type = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    # product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)

class ProductsAndPolicy(models.Model):
    prod_id = models.AutoField(primary_key=True)
    productandpolicy_name = models.CharField(max_length=50)
    prod_name = models.CharField(max_length=25)
    sub_product = models.CharField(max_length=25)
    customer_type = models.CharField(max_length=25)
    nationality = models.CharField(max_length=25)
    minimum_age = models.CharField(max_length=25)
    retirement_age = models.CharField(max_length=25)
    minimum_loan_amount = models.CharField(max_length=25)
    maximum_loan_amount = models.CharField(max_length=25)
    total_experience = models.CharField(max_length=25)
    effective_date = models.DateField(auto_now_add=True)
    ineffective_date = models.DateField(null = True)


    # otherdetails = models.ForeignKey(OtherDetails, on_delete=models.CASCADE)
    # property = models.ForeignKey(Property, on_delete=models.CASCADE)
    # ltv = models.ForeignKey(LoanTowardsValuation, on_delete=models.CASCADE)
    # fee = models.ForeignKey(Fees, on_delete=models.CASCADE)
    # obligations = models.ForeignKey(Obligation, on_delete=models.CASCADE)
    # income = models.ForeignKey(Income, on_delete=models.CASCADE)
    # designation = models.ForeignKey(CustomerDesignation, on_delete=models.CASCADE)
    company_type = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class CostSheet(models.Model):
    cost_particular_id = models.AutoField(primary_key=True)
    particulars = models.CharField(max_length=90)

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    # cust_type = models.CharField(max_length=15, default = "salaried")
    min_age = models.IntegerField()
    total_Exp = models.IntegerField()
    form16 = models.CharField(max_length=3)
    salary_type = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class CustomerDesignation(models.Model):
    cust_desig_id = models.AutoField(primary_key=True)
    cust_desig = models.CharField(max_length=25)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)


class CustomerNationality(models.Model):
    cust_nat_id = models.AutoField(primary_key=True)
    cust_nat = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class Fees(models.Model):
    fee_id = models.AutoField(primary_key=True)
    login_fees = models.CharField(max_length=25)
    proc_fee_app = models.CharField(max_length=25)
    proc_fee_type = models.CharField(max_length=25)
    proc_fee_flat_loan_amtwise = models.CharField(max_length=25)
    proc_fee_percent_loan_amtwise = models.CharField(max_length=25)
    offers = models.CharField(max_length=25)
    offline_or_online = models.CharField(max_length=7)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)


class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    gross_sal = models.CharField(max_length=25)
    net_sal = models.CharField(max_length=25)
    bonus = models.CharField(max_length=25)
    bonus_avg_yearly = models.CharField(max_length=25)
    bonus_avg_yearly_percent = models.CharField(max_length=25)
    bonus_avg_qtr = models.CharField(max_length=25)
    bonus_avg_qtr_percent = models.CharField(max_length=25)
    bonus_avg_half_yearly = models.CharField(max_length=25)
    bonus_avg_half_yearly_percent = models.CharField(max_length=25)
    rent_income = models.CharField(max_length=25)
    rent_agreement_type = models.CharField(max_length=25)
    bank_ref = models.CharField(max_length=25)
    rent_ref_in_bank = models.CharField(max_length=25)
    rent_inc_percent = models.CharField(max_length=25)
    fut_rent = models.CharField(max_length=25)
    fut_rent_percent = models.CharField(max_length=25)
    incentive = models.CharField(max_length=25)
    incen_avg_months = models.CharField(max_length=25)
    incen_percent = models.CharField(max_length=25)
    coApplicant_No_Income_only_Rent_income = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)


class IncomeFoir(models.Model):
    inc_foir_id = models.AutoField(primary_key=True)
    min_amt = models.IntegerField()
    max_amt = models.IntegerField()
    percent = models.IntegerField()
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class LoanAmount(models.Model):
    loan_id = models.AutoField(primary_key=True)
    min_loan_amt = models.IntegerField()
    max_loan_amt = models.IntegerField()
    total_Exp = models.IntegerField()
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class LoanTowardsValuation(models.Model):
    loan_tow_val_id = models.AutoField(primary_key=True)
    cost_sheet = models.CharField(max_length=90)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    rbi_guidelines = models.CharField(max_length=25)
    ammenity = models.CharField(max_length=25)
    additional = models.CharField(max_length=25)
    car_parking = models.CharField(max_length=25)
    car_parking_percent = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)

class LtvResale(models.Model):
    ltv_id = models.AutoField(primary_key=True)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    rbi_guidelines = models.IntegerField()
    doccument_cost = models.IntegerField()
    additional = models.IntegerField()
    car_parking = models.IntegerField()
    total = models.IntegerField()
    market_value = models.IntegerField()
    av_capping = models.IntegerField()
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class NegativeEmployerProfile(models.Model):
    neg_emp_pro_id = models.AutoField(primary_key=True)
    neg_emp_pro = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class NegativeArea(models.Model):
    neg_area_id = models.AutoField(primary_key=True)
    neg_area = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class Obligation(models.Model):
    obligation_id = models.AutoField(primary_key=True)
    emi_oblig = models.CharField(max_length=25)
    emi_oblig_not_consi = models.CharField(max_length=25)
    credit_card = models.CharField(max_length=25)
    credit_card_oblig_percent = models.IntegerField()
    gold_loan = models.CharField(max_length=25)
    gold_loan_percent = models.IntegerField()
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)

class OtherDetails(models.Model):
    oth_det_id = models.AutoField(primary_key=True)
    prevailing_rate = models.IntegerField()
    tenure = models.CharField(max_length=25)
    inward_cheque_return = models.CharField(max_length=25)
    multiple_inquiry = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)

class OtherDetailsROI(models.Model):
    oth_det_roi_id = models.AutoField(primary_key=True)
    min_loan_amt = models.IntegerField()
    max_loan_amt = models.IntegerField()
    min_val = models.IntegerField()
    max_val = models.IntegerField()
    roi_women = models.CharField(max_length=5)
    roi_men = models.CharField(max_length=5)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)


class Property(models.Model):
    prop_id = models.AutoField(primary_key=True)
    builder_cat = models.CharField(max_length=25)
    occupation_certi = models.CharField(max_length=25)
    prev_agreement = models.CharField(max_length=25)
    sub_scheme = models.CharField(max_length=25)
    perc_completion = models.IntegerField()
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)


class PropertyType(models.Model):
    prop_type_id = models.AutoField(primary_key=True)
    prop_type = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class RoomType(models.Model):
    romm_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class StageOfConstruction(models.Model):
    stage_id = models.AutoField(primary_key=True)
    stage = models.CharField(max_length=25)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

class Remarks(models.Model):
    remark_id = models.AutoField(primary_key=True)
    remark = models.CharField(max_length=25)

class BankCodes(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsAndPolicy, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=25)
    name_of_company = models.CharField(max_length=50)


class HlBasicDetails(models.Model): 
    customer_type               = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    nationality                 = models.CharField(max_length=50)
    minimum_age                 = models.IntegerField()
    retirement_age              = models.IntegerField()
    maximum_age_consider_govt   = models.IntegerField()
    maximum_age_consider_others = models.IntegerField()
    minimum_loan_amount         = models.FloatField()
    maximum_loan_amount         = models.FloatField()
    total_experience            = models.IntegerField()
    designation                 = models.ForeignKey(DesignationType, on_delete=models.CASCADE)
    company_type                = models.ForeignKey(CompanyType, on_delete=models.CASCADE)
    company_profitability       = models.BooleanField()
    form_16                     = models.BooleanField()
    salary_type                 = models.ForeignKey(SalaryType, on_delete=models.CASCADE)
    profession_tax_deduction    = models.BooleanField()
    negative_employer_profile   = models.BooleanField()

class HlObligation(models.Model): 
    emi_obligation                 = models.BooleanField()
    emi_obligation_not_consider    = models.IntegerField()
    credit_card                    = models.BooleanField()
    credit_card_obligation_percent = models.IntegerField()
    gold_loan                      = models.BooleanField()
    gold_loan_percent              = models.IntegerField()
    basic_details_id               = models.ForeignKey(HlBasicDetails,on_delete=models.CASCADE)


class HlOtherDetails(models.Model): 
    rate_of_interest      = models.IntegerField()
    prevailing_rate       = models.IntegerField()
    tenure                = models.IntegerField()
    inward_cheque_return  = models.BooleanField()
    multiple_inquiry      = models.BooleanField()
    relation_eligible     = models.CharField(max_length=25)
    relation_not_eligible = models.CharField(max_length=25)
    basic_details_id      = models.ForeignKey(HlBasicDetails,on_delete=models.CASCADE)


class HlProperty(models.Model): 
    builder_category              = models.BooleanField()
    apf                           = models.BooleanField()
    property_type                 = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    occupation_certificate        = models.BooleanField()
    cc_municipal_plan_tax_receipt = models.BooleanField()
    previous_aggrement_available  = models.BooleanField()
    subvention_scheme             = models.BooleanField()
    room_type                     = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    stage_of_construction         = models.ForeignKey(StageOfConstruction, on_delete=models.CASCADE)
    percent_of_completion         = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    negative_area                 = models.ForeignKey(NegativeArea, on_delete=models.CASCADE)
    property_age                  = models.IntegerField(blank=True, null=True)
    basic_details_id              = models.ForeignKey(HlBasicDetails,on_delete=models.CASCADE)


#From Builder
class HlLoan_To_Value_Type_1(models.Model): 
    loan_amount        = models.ForeignKey(LoanAmount, on_delete=models.CASCADE)
    rbi_guidelines     = models.IntegerField()
    amenity            = models.IntegerField()
    car_parking        = models.BooleanField()
    car_parking_amount = models.IntegerField(blank=True, null=True)
    basic_details_id   = models.ForeignKey(HlBasicDetails,on_delete=models.CASCADE)


#For Resale
class HlLoan_To_Value_Type_2(models.Model): 
    building_age                        = models.IntegerField()
    ltv_percent_for_fresh               = models.IntegerField()
    ltv_percent_for_balance_transfer    = models.IntegerField()
    tenure_percent_for_fresh            = models.IntegerField()
    tenure_percent_for_balance_transfer = models.IntegerField()
    basic_details_id                    = models.ForeignKey(HlBasicDetails,on_delete=models.CASCADE)

    
class HlIncome(models.Model): 
    gross_salary                            = models.BooleanField(default=None)
    net_salary                              = models.BooleanField(default=None)
    bonus                                   = models.BooleanField(default=None)
    bonus_avg_yearly                        = models.IntegerField()
    bonus_avg_yearly_percentage             = models.IntegerField()
    income_foir_yearly                      = models.BooleanField(default=None)
    bonus_avg_quarter                       = models.IntegerField()
    bonus_avg_quarter_percentage            = models.IntegerField()
    income_foir_quarter                     = models.BooleanField(default=None)
    bonus_avg_half_yearly                   = models.IntegerField()
    bonus_avg_half_yearly_percentage        = models.IntegerField()
    income_foir_half_yearly                 = models.BooleanField(default=None)
    rent_income                             = models.BooleanField(default=None)
    rent_agreement_type                     = models.CharField(max_length=25)
    bank_reflection                         = models.BooleanField(default=None)
    rent_reflection_in_bank                 = models.IntegerField()
    rent_income_percentage                  = models.IntegerField()
    co_applicant_no_income_only_rent_income = models.BooleanField(default=None)
    co_applicant_mandatory                  = models.BooleanField(default=None)
    future_rent                             = models.BooleanField(default=None)
    future_rent_percentage                  = models.IntegerField()
    income_foir_future_rent                 = models.IntegerField()
    incentive                               = models.BooleanField(default=None)
    incentive_avg_months                    = models.IntegerField()
    income_foir_incentive                   = models.BooleanField(default=None)
    income_foir                             = models.IntegerField()
    basic_details_id                        = models.ForeignKey(HlBasicDetails,on_delete=models.CASCADE)
