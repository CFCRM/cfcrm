from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from master.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

YES_NO_CHOICES = (
    (None,('Select Yes Or No')),
    (True, ('Yes')),
    (False, ('No'))
)

GOOD_BAD_CHOICES = (
  (None, '-- Good or Bad --'),
  ('Good', 'Good'),
  ('Bad', 'Bad')
)

KNOWN_UNKNOWN_CHOICES = (
  (None, '-- Select Cibil Type --'),
  ('1', 'Known'),
  ('2', 'Unknown')
)

DEFAULT_YEAR_CHOICES = (
    ('1', '-- Select --'),
    ('Last 12 Months', 'Last 12 Months'),
    ('Past', 'Past')
)

MARITAL_STATUS_CHOICES = (
    ('1', '-- Select MARITAL STATUS --'),
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('divorced', 'Divorced')
)

GENDER_CHOICES = (
  ('1', '-- Select Gender --'),
  ('Male', 'Male'),
  ('Female', 'Female'),
  ('Others', 'Others')
)

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year
# Create your models here.
class CustomUser(AbstractUser): 
    role            = models.CharField(max_length=20)
    phone           = models.CharField(max_length=10)
    alt_phone       = models.CharField(max_length=10)
    designation     = models.CharField(max_length=50)
    address         = models.TextField()
    mapped_to       = models.CharField(max_length=50)
    mapped_to_name  = models.CharField(max_length=10)
    type_of_partner = models.CharField(max_length=20, default='Hot')
    status          = models.CharField(max_length=20, default='Active')
    remarks         = models.CharField(max_length=20, default='good')
    by_online       = models.CharField(max_length=3)
    agreement       = models.FileField(upload_to='agreements', default="terms.pdf")


class Leads(models.Model): 
    prefix      = models.ForeignKey(Prefix, on_delete=models.CASCADE)
    name        = models.CharField(max_length=25)
    phone       = models.CharField(max_length=10)
    alt_phone   = models.CharField(max_length=10)
    email       = models.EmailField()
    reference   = models.CharField(max_length=50)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    sub_product = models.ForeignKey(SubProduct, on_delete=models.CASCADE)
    loan_amt    = models.IntegerField()
    address     = models.TextField()
    pincode     = models.CharField(max_length=6)
    state       = models.ForeignKey(State, on_delete=models.CASCADE)
    city        = models.ForeignKey(City, on_delete=models.CASCADE)
    added_by    = models.CharField(max_length=50, null=True)


class AdditionalDetails(models.Model): 
    cust_name        = models.CharField(max_length=25)
    is_diff          = models.BooleanField(blank = True)
    cust_type        = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    inc_holder       = models.BooleanField(null=False,choices=YES_NO_CHOICES)
    prop_owner       = models.BooleanField(null = False,choices=YES_NO_CHOICES)
    applicant_type   = models.ForeignKey(ApplicantType, on_delete=models.CASCADE)
    relation         = models.ForeignKey(Relation, on_delete=models.CASCADE)
    lead_id          = models.ForeignKey(Leads, on_delete=models.CASCADE)
    con_phone        = models.CharField(max_length=10)
    con_person_name  = models.CharField(max_length=25,blank= True)
    con_person_phone = models.CharField(max_length=10,blank= True)


class SalPersonalDetails(models.Model): 
    per_det_id            = models.AutoField(primary_key=True)
    loan_amount           = models.IntegerField(null=True)
    cibil_type            = models.ForeignKey(CibilType, on_delete=models.CASCADE, blank=True, null=True)
    cibil_score           = models.IntegerField(null=True, blank=True)
    loan_taken            = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    repayment_history     = models.CharField(max_length=4, choices=GOOD_BAD_CHOICES, default=None, blank=True, null=True)
    product_id            = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    default_year          = models.ForeignKey(DefaultYear, on_delete=models.CASCADE, blank=True, null=True)
    details_about_default = models.CharField(max_length=200, blank=True)
    gender                = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    dob                   = models.DateField(blank=True, null=True)
    age                   = models.IntegerField()
    retirement_age        = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(50), MaxValueValidator(70)])
    marital_status        = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, blank=True, null=True)
    qualification         = models.ForeignKey(Qualification, on_delete=models.CASCADE, blank=True, null=True)  
    degree_others         = models.CharField(max_length=100, blank=True, null=True)
    profession            = models.ForeignKey(Profession, on_delete=models.CASCADE, blank=True, null=True)
    degree                = models.ForeignKey(Degree, on_delete=models.CASCADE, blank=True, null=True)
    lawyerType            = models.ForeignKey(LawyerType, on_delete=models.CASCADE, blank=True, null=True)
    nationality           = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null=True)
    country               = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    enduse                = models.CharField(max_length=200, blank=True, null=True)
    additional_details_id = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE, blank=True, null=True)
    # proof                 = models.CharField(max_length=1)
    # consi_age             = models.IntegerField(max_length=3, null=True)
       

class SalIncomeDetails(models.Model): 
    inc_det_id         = models.AutoField(primary_key=True)
    salary_type        = models.ForeignKey(SalaryType, on_delete=models.CASCADE, blank=True, null=True)
    bank_name          = models.ForeignKey(BankName, on_delete=models.CASCADE)
    gross_sal          = models.IntegerField()
    net_sal            = models.IntegerField()
    bonus_duration     = models.IntegerField(blank=True, null=True)
    bonus_amount       = models.IntegerField(blank=True, null=True)
    incentive_duration = models.IntegerField(blank=True, null=True)
    incentive_amount   = models.IntegerField(blank=True, null=True)
    deduction          = models.ForeignKey(DeductionType, on_delete=models.CASCADE, blank=True, null=True)
    deduction_choice   = models.BooleanField(choices=YES_NO_CHOICES, blank=True, null=True)
    addi_details_id    = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)
    # bonus_tenure       = models.IntegerField()


class SalOtherIncomes(models.Model): 
    other_inc_id               = models.AutoField(primary_key=True)
    rental_income              = models.IntegerField()
    lessee_type                = models.ForeignKey(LesseType, on_delete=models.CASCADE, blank=True, null=True)
    lessee_name                = models.CharField(max_length=50, blank=True, null=True)
    rent_amount                = models.IntegerField()
    tenure_of_agreement        = models.IntegerField()
    tenure_pending             = models.IntegerField()
    valid_rent_agreement       = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    will_you_make_agreement    = models.BooleanField(choices=YES_NO_CHOICES, blank=True, null=True)
    how_old_is_agreement       = models.IntegerField(blank=True, null=True)
    agreement_type             = models.ForeignKey(AgreementType, on_delete=models.CASCADE, blank=True, null=True)
    reflection_in_bank_account = models.BooleanField(choices=YES_NO_CHOICES, blank=True, null=True)
    rent_reflection_in_bank    = models.IntegerField()
    reflection_in_itr          = models.BooleanField(choices=YES_NO_CHOICES, blank=True, null=True)
    extension_expected_years   = models.IntegerField()
    addi_details_id            = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class SalAdditionalOtherIncomes(models.Model): 
    add_oth_inc_id  = models.AutoField(primary_key=True)
    other_income    = models.CharField(max_length=50)
    income_amount   = models.IntegerField()
    addi_details_id = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)

class ContactPerson(models.Model):
    name = models.CharField(max_length=20)


class SalCompanyDetails(models.Model): 
    comp_det_id        = models.AutoField(primary_key=True)
    company_type       = models.ForeignKey(CompanyType, on_delete=models.CASCADE, blank=True, null=True)
    company_name       = models.ForeignKey(CompanyName, on_delete=models.CASCADE, blank=True, null=True)
    location           = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    paid_up_capital    = models.IntegerField()
    company_age        = models.IntegerField()
    nature_of_business = models.CharField(max_length=50)
    designation        = models.CharField(max_length=50)
    designation_type   = models.ForeignKey(DesignationType, on_delete=models.CASCADE, blank=True, null=True)
    current_experience = models.IntegerField()
    total_experience   = models.IntegerField()
    employment_type    = models.ForeignKey(EmploymentType, on_delete=models.CASCADE, blank=True, null=True)
    form_16            = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    office_phone       = models.CharField(max_length=10)
    office_email       = models.EmailField(max_length=50)
    addi_details_id    = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE, blank=True, null=True)


class SalExistingLoanDetails(models.Model): 
    existing_loan_det_id                = models.AutoField(primary_key=True)
    bank_name                           = models.ForeignKey(BankName, on_delete=models.CASCADE)
    products_or_services                = models.ForeignKey(ProductsOrServices, on_delete=models.CASCADE)
    loan_amount                         = models.IntegerField()
    emi                                 = models.DecimalField(max_digits=12, decimal_places=2)
    rate_of_interest                    = models.DecimalField(max_digits=12, decimal_places=2)
    tenure                              = models.IntegerField()
    emi_start_date                      = models.DateField()
    emi_end_date                        = models.DateField()
    outstanding_amount_paid_by_customer = models.IntegerField()
    outstanding_amount                  = models.IntegerField()
    any_bounces                         = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    moratorium_taken                    = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    applicant_type                      = models.ForeignKey(ApplicantType, on_delete=models.CASCADE)
    addi_details_id                     = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class SalExistingCreditCard(models.Model): 
    existing_credit_card_id = models.AutoField(primary_key=True)
    bank_name               = models.ForeignKey(BankName, on_delete=models.CASCADE)
    credit_limit            = models.IntegerField()
    limit_utilized          = models.IntegerField()
    minimum_due             = models.DecimalField(max_digits=12, decimal_places=2)
    credit_card_age         = models.IntegerField()
    payment_delay           = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    payment_delay_year      = models.ForeignKey(PaymentDelayYear, on_delete=models.CASCADE)
    moratorium_taken        = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    addi_details_id         = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class SalAdditionalDetails(models.Model): 
    sal_add_det_id                    = models.AutoField(primary_key=True)
    inward_cheque_return              = models.IntegerField()
    loan_inquiry_disbursement         = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    loan_inquiry_disbursement_details = models.TextField(blank=True, null=True)
    addi_details_id                   = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)

class SalInvestments(models.Model): 
    sal_inv_id      = models.AutoField(primary_key=True)
    investments     = models.ForeignKey(InvestmentType, on_delete=models.CASCADE)
    addi_details_id = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class SalResidenceDetails(models.Model):
    sal_res_det_id         = models.AutoField(primary_key=True)
    current_residence_type = models.ForeignKey(ResidenceType, on_delete=models.CASCADE)
    state                  = models.ForeignKey(State, on_delete=models.CASCADE)
    current_location_city  = models.ForeignKey(City, on_delete=models.CASCADE)
    addi_details_id        = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)

#--------------------------------------------------------Property Details--------------------------------------------------------------#

class PropertyDetails(models.Model): 
    pass
#     prop_det_id = models.AutoField(primary_key=True)
#     prop_type   = models.CharField(max_length=50)
#     lead_id     = models.ForeignKey(Leads, on_delete=models.CASCADE)


class PropType1(models.Model): #Underconstruction buying from builder
    builder_name        = models.CharField(max_length=50)
    proj_name           = models.CharField(max_length=50)
    apf_num             = models.CharField(max_length=50)
    apf_approved_lender = models.ManyToManyField(BankName)
    const_stage         = models.CharField(max_length=50)
    per_complete        = models.FloatField()
    possession_date     = models.DateField()
    total_floors        = models.IntegerField()
    buy_floor           = models.IntegerField()
    slabs_done          = models.IntegerField()
    agreement_val       = models.IntegerField()
    market_val          = models.IntegerField()
    prop_loc            = models.CharField(max_length=50)
    prop_city           = models.ForeignKey(City,on_delete=models.CASCADE)
    prop_state          = models.ForeignKey(State,on_delete=models.CASCADE)
    prop_in             = models.ForeignKey(PropertyIn,on_delete=CASCADE)
    cc_rec              = models.BooleanField( choices = YES_NO_CHOICES )
    cc_rec_upto         = models.IntegerField(blank=True, null=True)
    municipal_approved  = models.BooleanField( choices = YES_NO_CHOICES )
    area_size           = models.IntegerField()
    area_in             = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
    area_type           = models.ForeignKey(AreaType,on_delete=models.CASCADE)
    room_type           = models.ForeignKey(RoomType,on_delete= models.CASCADE)
    agreement_type      = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
    pay_till_date       = models.DecimalField( max_digits=12, decimal_places=2)
    stamp_duty          = models.BooleanField( choices = YES_NO_CHOICES )
    stamp_duty_amt      = models.CharField(max_length=10)
    cost_sheet          = models.BooleanField(choices = YES_NO_CHOICES,default = True)
    cost_sheet_amt      = models.CharField(max_length=7,blank=True,null=True)
    lead_id             = models.ForeignKey(Leads,on_delete=models.CASCADE)
    future_rent         = models.IntegerField()
    car_parking_amt     = models.IntegerField(blank=True, null=True)
    subvention_scheme   = models.BooleanField(choices = YES_NO_CHOICES,blank=True, null=True)
    car_parking         = models.BooleanField(choices = YES_NO_CHOICES)

class PropType2(models.Model):# Underconstruction buying from seller
    seller_status       = models.ForeignKey(Status,on_delete=models.CASCADE)
    builder_name        = models.CharField(max_length=50)
    proj_name           = models.CharField(max_length=50)
    apf_num             = models.CharField(max_length=50)
    apf_approved_lender = models.ManyToManyField(BankName)
    const_stage         = models.CharField(max_length=50)
    per_complete        = models.FloatField()
    possession_date     = models.DateField()
    total_floors        = models.IntegerField()
    buy_floor           = models.IntegerField()
    slabs_done          = models.IntegerField()
    agreement_val       = models.IntegerField()
    market_val          = models.IntegerField()
    prop_loc            = models.CharField(max_length=50)
    prop_city           = models.ForeignKey(City,on_delete=models.CASCADE)
    prop_state          = models.ForeignKey(State,on_delete=models.CASCADE)
    prop_in             = models.ForeignKey(PropertyIn,on_delete=CASCADE)
    cc_rec              = models.BooleanField( choices = YES_NO_CHOICES )
    cc_rec_upto         = models.IntegerField(blank=True,null=True)
    municipal_approved  = models.BooleanField( choices = YES_NO_CHOICES )
    area_size           = models.IntegerField()
    area_in             = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
    area_type           = models.ForeignKey(AreaType,on_delete=models.CASCADE)
    room_type           = models.ForeignKey(RoomType,on_delete= models.CASCADE)
    agreement_type      = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
    pay_till_date       = models.CharField(blank=True, null=True,max_length=20)
    stamp_duty          = models.BooleanField( choices = YES_NO_CHOICES )
    stamp_duty_amt      = models.IntegerField()
    cost_sheet          = models.BooleanField(default = False,choices = YES_NO_CHOICES)
    cost_sheet_amt      = models.IntegerField(blank=True, null=True)
    lead_id             = models.ForeignKey(Leads,on_delete=models.CASCADE)
    future_rent         = models.IntegerField()
    car_parking_amt     = models.IntegerField(blank=True, null=True)
    car_parking         = models.BooleanField(choices = YES_NO_CHOICES)


class PropType3(models.Model):
    builder_name        = models.CharField(max_length=50)
    proj_name           = models.CharField(max_length=50)
    apf_num             = models.CharField(max_length=50)
    apf_approved_lender = models.ManyToManyField(BankName)
    total_floors        = models.IntegerField()
    buy_floor           = models.IntegerField()
    building_age        = models.IntegerField()
    agreement_val       = models.IntegerField()
    market_val          = models.IntegerField()
    prop_loc            = models.CharField(max_length=50)
    prop_city           = models.ForeignKey(City,on_delete=models.CASCADE)
    prop_state          = models.ForeignKey(State,on_delete=models.CASCADE)
    prop_in             = models.ForeignKey(PropertyIn,on_delete=CASCADE)
    cc_rec              = models.BooleanField( choices = YES_NO_CHOICES )
    oc_rec              = models.BooleanField( choices = YES_NO_CHOICES )
    municipal_approved  = models.BooleanField( choices = YES_NO_CHOICES )
    area_size           = models.IntegerField()
    area_in             = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
    area_type           = models.ForeignKey(AreaType,on_delete=models.CASCADE)
    room_type           = models.ForeignKey(RoomType,on_delete= models.CASCADE)
    agreement_type      = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
    pay_till_date       = models.CharField(max_length=10)
    stamp_duty          = models.BooleanField( choices = YES_NO_CHOICES )
    stamp_duty_amt      = models.IntegerField(blank=True, null=True)
    cost_sheet          = models.BooleanField( choices = YES_NO_CHOICES)
    cost_sheet_amt      = models.IntegerField(blank=True, null=True)
    lead_id             = models.ForeignKey(Leads,on_delete=models.CASCADE)
    car_parking_amt     = models.IntegerField(blank=True, null=True)
    car_parking         = models.BooleanField(choices = YES_NO_CHOICES)


# #  Ready possession buying from seller
class PropType4(models.Model):
    seller_status                        = models.ForeignKey(Status,on_delete=CASCADE)
    name_of_seller                       = models.CharField(max_length=50)
    project_name                         = models.CharField(max_length=50)
    apf_num                              = models.CharField(max_length=50)
    apf_approved_lender                  = models.ManyToManyField(BankName)
    total_floors                         = models.IntegerField()
    buy_floor                            = models.IntegerField()
    building_age                         = models.IntegerField()
    agreement_val                        = models.IntegerField()
    market_val                           = models.IntegerField()
    prop_loc                             = models.CharField(max_length=50)
    prop_city                            = models.ForeignKey(City,on_delete=models.CASCADE)
    prop_state                           = models.ForeignKey(State,on_delete=models.CASCADE)
    prop_in                              = models.ForeignKey(PropertyIn,on_delete=CASCADE)
    cc_available                         = models.BooleanField( choices = YES_NO_CHOICES )
    oc_rec                               = models.BooleanField( choices = YES_NO_CHOICES )
    oc_rec_floor                         = models.IntegerField(blank=True, null=True)
    municipal_approved                   = models.BooleanField( choices = YES_NO_CHOICES )
    area_size                            = models.IntegerField()
    area_in                              = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
    area_type                            = models.ForeignKey(AreaType,on_delete=models.CASCADE)
    room_type                            = models.ForeignKey(RoomType,on_delete= models.CASCADE)
    agreement_type                       = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
    pay_till_date                        = models.CharField(max_length=10)
    previous_aggrement_available         = models.BooleanField(null=True ,blank=True, choices=YES_NO_CHOICES)
    registration_done_previous_aggremnet = models.CharField(max_length=100)
    concern_area                         = models.CharField(max_length=100)
    stamp_duty_registration_paid         = models.BooleanField(choices=YES_NO_CHOICES)
    stamp_duty_amt                       = models.IntegerField(blank=True, null=True)
    property_tax_paid                    = models.BooleanField(null=True,blank=True,choices = YES_NO_CHOICES)
    society_informed                     = models.BooleanField(null=True,blank=True,choices = YES_NO_CHOICES)
    car_parking_amt                      = models.IntegerField(blank=True, null=True)
    car_parking                          = models.BooleanField(choices = YES_NO_CHOICES)
    lead_id                              = models.ForeignKey(Leads,on_delete=models.CASCADE)



#--------------------------------------------------------Student Details--------------------------------------------------------------#


class StudentDetails(models.Model): 
    student_id  = models.AutoField(primary_key=True)
    dob         = models.DateField()
    age         = models.CharField(max_length=3)
    phone       = models.CharField(max_length=10)
    alt_phone   = models.CharField(max_length=10)
    email       = models.CharField(max_length=30)
    gender      = models.CharField(max_length=6)
    location    = models.CharField(max_length=20)
    state       = models.CharField(max_length=20)
    pincode     = models.CharField(max_length=6)
    nationality = models.CharField(max_length=10)
    country     = models.CharField(max_length=10)
    end_use     = models.CharField(max_length=10)
    add_det_id  = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class StudentExistingLoanDetails(models.Model): 
    loan_det_id      = models.AutoField(primary_key=True)
    bank_name        = models.CharField(max_length=20)
    product          = models.CharField(max_length=10)
    loan_amt         = models.CharField(max_length=10)
    emi              = models.CharField(max_length=10)
    roi              = models.CharField(max_length=3)
    tenure           = models.CharField(max_length=3)
    emi_start_date   = models.DateField()
    emi_end_date     = models.DateField()
    outstanding_paid = models.CharField(max_length=10)
    outstanding_amt  = models.CharField(max_length=10)
    any_bounce       = models.CharField(max_length=10)
    moratorium_taken = models.CharField(max_length=10)
    applicant_type   = models.CharField(max_length=10)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class StudentExistingCardDetails(models.Model): 
    card_id          = models.AutoField(primary_key=True)
    bank_name        = models.CharField(max_length=20)
    credit_limit     = models.CharField(max_length=20)
    limit_utilized   = models.CharField(max_length=20)
    min_due          = models.CharField(max_length=20)
    card_age         = models.CharField(max_length=3)
    pay_delay        = models.CharField(max_length=5)
    pay_delay_year   = models.CharField(max_length=20)
    moratorium_taken = models.CharField(max_length=20)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)

#--------------------------------------------------------SHouseWife Details--------------------------------------------------------------#


class HousewifeDetails(models.Model): 
    hw_id       = models.AutoField(primary_key=True)
    dob         = models.DateField()
    age         = models.CharField(max_length=3)
    phone       = models.CharField(max_length=10)
    alt_phone   = models.CharField(max_length=10)
    email       = models.CharField(max_length=30)
    gender      = models.CharField(max_length=6)
    address     = models.CharField(max_length=20)
    state       = models.CharField(max_length=20)
    pincode     = models.CharField(max_length=6)
    nationality = models.CharField(max_length=10)
    country     = models.CharField(max_length=10)
    end_use     = models.CharField(max_length=10)
    add_det_id  = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class HousewifePersonalDetails(models.Model): 
    hw_per_det_id     = models.AutoField(primary_key=True)
    loan_Amt          = models.CharField(max_length=10)
    cibil_type        = models.CharField(max_length=10)
    cibil_score       = models.CharField(max_length=10)
    loan_cc           = models.CharField(max_length=10)
    repayment_history = models.CharField(max_length=10)
    default_year      = models.CharField(max_length=10)
    details_default   = models.CharField(max_length=10)
    add_det_id        = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class HousewifeExistingLoanDetails(models.Model): 
    loan_det_id      = models.AutoField(primary_key=True)
    bank_name        = models.CharField(max_length=20)
    product          = models.CharField(max_length=10)
    loan_amt         = models.CharField(max_length=10)
    emi              = models.CharField(max_length=10)
    roi              = models.CharField(max_length=3)
    tenure           = models.CharField(max_length=3)
    emi_start_date   = models.DateField()
    emi_end_date     = models.DateField()
    outstanding_paid = models.CharField(max_length=10)
    outstanding_amt  = models.CharField(max_length=10)
    any_bounce       = models.CharField(max_length=10)
    moratorium_taken = models.CharField(max_length=10)
    applicant_type   = models.CharField(max_length=10)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class HousewifeExistingCardDetails(models.Model): 
    card_id          = models.AutoField(primary_key=True)
    bank_name        = models.CharField(max_length=20)
    credit_limit     = models.CharField(max_length=20)
    limit_utilized   = models.CharField(max_length=20)
    min_due          = models.CharField(max_length=20)
    card_age         = models.CharField(max_length=3)
    pay_delay        = models.CharField(max_length=5)
    pay_delay_year   = models.CharField(max_length=20)
    moratorium_taken = models.CharField(max_length=20)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class HousewifeInvestmentDetails(models.Model): 
    invest_id  = models.AutoField(primary_key=True)
    investment = models.CharField(max_length=30)
    add_det_id = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)

#-------------------------------------------------------- Retired Details--------------------------------------------------------------#


class RetiredDetails(models.Model): 
    retired_id  = models.AutoField(primary_key=True)
    dob         = models.DateField()
    age         = models.CharField(max_length=3)
    phone       = models.CharField(max_length=10)
    alt_phone   = models.CharField(max_length=10)
    email       = models.CharField(max_length=30)
    gender      = models.CharField(max_length=6)
    address     = models.CharField(max_length=20)
    state       = models.CharField(max_length=20)
    pincode     = models.CharField(max_length=6)
    nationality = models.CharField(max_length=10)
    country     = models.CharField(max_length=10)
    end_use     = models.CharField(max_length=10)
    add_det_id  = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class RetiredPensionDetails(models.Model): 
    pension_id   = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    bank_name    = models.CharField(max_length=50)
    net_pension  = models.CharField(max_length=10)
    add_det_id   = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class RetiredResidenceDetails(models.Model): 
    res_id           = models.AutoField(primary_key=True)
    res_type         = models.CharField(max_length=50)
    current_location = models.CharField(max_length=50)
    state            = models.CharField(max_length=50)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class RetiredExistingLoanDetails(models.Model): 
    loan_det_id      = models.AutoField(primary_key=True)
    bank_name        = models.CharField(max_length=20)
    product          = models.CharField(max_length=10)
    loan_amt         = models.CharField(max_length=10)
    emi              = models.CharField(max_length=10)
    roi              = models.CharField(max_length=3)
    tenure           = models.CharField(max_length=3)
    emi_start_date   = models.DateField()
    emi_end_date     = models.DateField()
    outstanding_paid = models.CharField(max_length=10)
    outstanding_amt  = models.CharField(max_length=10)
    any_bounce       = models.CharField(max_length=10)
    moratorium_taken = models.CharField(max_length=10)
    applicant_type   = models.CharField(max_length=10)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class RetiredExistingCardDetails(models.Model): 
    card_id          = models.AutoField(primary_key=True)
    bank_name        = models.CharField(max_length=20)
    credit_limit     = models.CharField(max_length=20)
    limit_utilized   = models.CharField(max_length=20)
    min_due          = models.CharField(max_length=20)
    card_age         = models.CharField(max_length=3)
    pay_delay        = models.CharField(max_length=5)
    pay_delay_year   = models.CharField(max_length=20)
    moratorium_taken = models.CharField(max_length=20)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class RetiredInvestmentDetails(models.Model): 
    invest_id  = models.AutoField(primary_key=True)
    investment = models.CharField(max_length=30)
    add_det_id = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class RetiredOtherDetails(models.Model): 
    other_det_id     = models.AutoField(primary_key=True)
    inward_cheque    = models.CharField(max_length=30)
    multiple_enquiry = models.CharField(max_length=30)
    add_det_id       = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)
