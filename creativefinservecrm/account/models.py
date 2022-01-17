from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from master.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

CHOICES_BOOLEAN = (
    (True, ('Yes')),
    (False, ('No'))
)
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
    inc_holder       = models.BooleanField(null=False,choices=CHOICES_BOOLEAN)
    prop_owner       = models.BooleanField(null = False,choices=CHOICES_BOOLEAN)
    applicant_type   = models.ForeignKey(ApplicantType, on_delete=models.CASCADE)
    relation         = models.ForeignKey(Relation, on_delete=models.CASCADE)
    lead_id          = models.ForeignKey(Leads, on_delete=models.CASCADE)
    con_phone        = models.CharField(max_length=10)
    con_person_name  = models.CharField(max_length=25,blank= True)
    con_person_phone = models.CharField(max_length=10,blank= True)
class PersonalDetails(models.Model): 
    per_det_id            = models.AutoField(primary_key=True)
    loan_amount           = models.IntegerField(null=True)
    cibil_type            = models.ForeignKey(CibilType, on_delete=models.CASCADE)
    cibil_score           = models.IntegerField(null=True, blank=True)
    loan_taken            = models.BooleanField(choices=YES_NO_CHOICES)
    product_id            = models.ForeignKey(Product, on_delete=models.CASCADE)
    repayment_history     = models.ForeignKey(RepaymentHistory, on_delete=models.CASCADE)
    default_year          = models.ForeignKey(DefaultYear, on_delete=models.CASCADE)
    details_about_default = models.CharField(max_length=200)
    gender                = models.ForeignKey(Gender, on_delete=models.CASCADE)
    dob                   = models.DateField(blank=True, null=True)
    age                   = models.IntegerField(blank=True, null=True)
    retirement_age        = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(50), MaxValueValidator(70)])
    marital_status        = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, blank=True, null=True)
    qualification         = models.ForeignKey(Qualification, on_delete=models.CASCADE)  
    degree_others         = models.CharField(max_length=100, blank=True, null=True)
    profession            = models.ForeignKey(Profession, on_delete=models.CASCADE)
    degree                = models.ForeignKey(Degree, on_delete=models.CASCADE, blank=True, null=True)
    lawyerType            = models.ForeignKey(LawyerType, on_delete=models.CASCADE, blank=True, null=True)
    nationality           = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    country               = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    enduse                = models.CharField(max_length=200)
    additional_details_id = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)
    # proof                 = models.CharField(max_length=1)
    # consi_age             = models.IntegerField(max_length=3, null=True)
       

class SalIncomeDetails(models.Model): 
    inc_det_id          = models.AutoField(primary_key=True)
    salaryType          = models.CharField(max_length=50)
    bank_name           = models.CharField(max_length=70)
    gross_sal           = models.CharField(max_length=10)
    net_sal             = models.CharField(max_length=10)
    bonusType           = models.CharField(max_length=50)
    bonus_amt           = models.CharField(max_length=10)
    bonus_tenure        = models.IntegerField()
    incentivesType      = models.CharField(max_length=50)
    incentive_amt       = models.CharField(max_length=10)
    addi_details_id_inc = models.ForeignKey(
        AdditionalDetails, on_delete=models.CASCADE)


class SalOtherIncomes(models.Model): 
    other_inc_det_id            = models.AutoField(primary_key=True)
    rental_income               = models.CharField(max_length=10)
    Lessee_Type                 = models.CharField(max_length=50)
    Lessee_Name                 = models.CharField(max_length=50)
    rent_amount                 = models.CharField(max_length=10)
    tenure_of_arguement         = models.CharField(max_length=10)
    tenure_pending              = models.CharField(max_length=10)
    valid_rent_agreement        = models.CharField(max_length=10)
    Will_u_make_agreement       = models.CharField(max_length=10)
    How_old_is_agreement        = models.CharField(max_length=50)
    agreement_Type              = models.CharField(max_length=50)
    reflection_in_bank_acc      = models.CharField(max_length=10)
    reflection_in_ITR_acc       = models.CharField(max_length=100)
    extension_expected_in_years = models.CharField(max_length=70)
    addi_details_id_other_inc   = models.ForeignKey(
        AdditionalDetails, on_delete=models.CASCADE)


class SalAdditonalOtherIncome(models.Model): 
    add_oth_inc_det_id = models.AutoField(primary_key=True)
    other_income       = models.CharField(max_length=50)
    income_amount      = models.CharField(max_length=10)
    add_det_id         = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)

class ContactPerson(models.Model):
    name = models.CharField(max_length=20)
class SalCompanyDetails(models.Model): 
    comp_det_id     = models.AutoField(primary_key=True)
    comp_type       = models.CharField(max_length=50)
    comp_name       = models.CharField(max_length=50)
    location        = models.CharField(max_length=50)
    paid_up_cap     = models.CharField(max_length=10)
    comp_age        = models.CharField(max_length=3)
    nature_business = models.CharField(max_length=50)
    designation     = models.CharField(max_length=50)
    des_type        = models.CharField(max_length=50)
    curr_exp        = models.CharField(max_length=3)
    total_exp       = models.CharField(max_length=3)
    emp_type        = models.CharField(max_length=50)
    form16          = models.CharField(max_length=3)
    office_phone    = models.CharField(max_length=11)
    office_email    = models.CharField(max_length=50)
    add_det_id      = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class SalExistingLoanDetails(models.Model): 
    existing_loan_det_id     = models.AutoField(primary_key=True)
    bank_name                = models.CharField(max_length=50)
    products                 = models.CharField(max_length=100)
    loan_amount              = models.CharField(max_length=10)
    emi                      = models.CharField(max_length=10)
    rate_of_interest         = models.CharField(max_length=5)
    tenure                   = models.CharField(max_length=50)
    emi_start_date           = models.CharField(max_length=50)
    emi_end_date             = models.DateField()
    outstan_paid_by_customer = models.CharField(max_length=10)
    outstanding_amount       = models.CharField(max_length=10)
    any_bounces              = models.CharField(max_length=50)
    moratorium_taken         = models.CharField(max_length=10)
    application_type         = models.CharField(max_length=10)
    add_det_id               = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class SalExistingCardDetails(models.Model): 
    existing_card_det_id = models.AutoField(primary_key=True)
    card_bank_name       = models.CharField(max_length=50)
    credit_limit         = models.CharField(max_length=100)
    limit_utilized       = models.CharField(max_length=10)
    min_due              = models.CharField(max_length=10)
    credit_card_age      = models.CharField(max_length=5)
    payment_delay        = models.CharField(max_length=50)
    payment_delay_year   = models.CharField(max_length=50)
    mor_taken            = models.CharField(max_length=50)
    add_det_id           = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class SalAdditionalDetails(models.Model): 
    sal_add_det_id    = models.AutoField(primary_key=True)
    inw_cheque_return = models.CharField(max_length=50)
    loan_enq_disburse = models.CharField(max_length=100)
    loan_enq_det      = models.CharField(max_length=100)
    add_det_id        = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


class Investments(models.Model): 
    sal_inv_id         = models.AutoField(primary_key=True)
    investments_u_have = models.CharField(max_length=50)
    add_det_id         = models.ForeignKey(AdditionalDetails, on_delete=models.CASCADE)


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
    per_complete        = models.CharField(max_length=3)
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
    cc_rec              = models.BooleanField( choices = CHOICES_BOOLEAN )
    cc_rec_upto         = models.IntegerField()
    municipal_approved  = models.BooleanField( choices = CHOICES_BOOLEAN )
    area_size           = models.IntegerField()
    area_in             = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
    area_type           = models.ForeignKey(AreaType,on_delete=models.CASCADE)
    room_type           = models.ForeignKey(RoomType,on_delete= models.CASCADE)
    agreement_type      = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
    pay_till_date       = models.CharField(max_length=10)
    stamp_duty          = models.BooleanField( choices = CHOICES_BOOLEAN )
    stamp_duty_amt      = models.CharField(max_length=10)
    cost_sheet          = models.CharField(max_length=3)
    cost_sheet_amt      = models.CharField(max_length=7)
    lead_id             = models.ForeignKey(Leads,on_delete=models.CASCADE)
    future_rent         = models.IntegerField()
    car_parking_amt     = models.IntegerField()
    subvention_scheme   = models.BooleanField(choices = CHOICES_BOOLEAN)
    car_parking         = models.BooleanField(choices = CHOICES_BOOLEAN)

class PropType2(models.Model):# Underconstruction buying from seller
    seller_status       = models.ForeignKey(Status,on_delete=models.CASCADE)
    builder_name        = models.CharField(max_length=50)
    proj_name           = models.CharField(max_length=50)
    apf_num             = models.CharField(max_length=50)
    apf_approved_lender = models.ManyToManyField(BankName)
    const_stage         = models.CharField(max_length=50)
    per_complete        = models.CharField(max_length=3)
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
    cc_rec              = models.BooleanField( choices = CHOICES_BOOLEAN )
    cc_rec_upto         = models.IntegerField()
    municipal_approved  = models.BooleanField( choices = CHOICES_BOOLEAN )
    area_size           = models.IntegerField()
    area_in             = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
    area_type           = models.ForeignKey(AreaType,on_delete=models.CASCADE)
    room_type           = models.ForeignKey(RoomType,on_delete= models.CASCADE)
    agreement_type      = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
    pay_till_date       = models.CharField(max_length=10)
    stamp_duty          = models.BooleanField( choices = CHOICES_BOOLEAN )
    stamp_duty_amt      = models.CharField(max_length=10)
    cost_sheet          = models.CharField(max_length=3)
    cost_sheet_amt      = models.CharField(max_length=7)
    lead_id             = models.ForeignKey(Leads,on_delete=models.CASCADE)
    future_rent         = models.IntegerField()
    car_parking_amt     = models.IntegerField()
    car_parking         = models.BooleanField(choices = CHOICES_BOOLEAN)


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
   cc_rec              = models.BooleanField( choices = CHOICES_BOOLEAN )
   oc_rec              = models.BooleanField( choices = CHOICES_BOOLEAN )
   municipal_approved  = models.BooleanField( choices = CHOICES_BOOLEAN )
   area_size           = models.IntegerField()
   area_in             = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
   area_type           = models.ForeignKey(AreaType,on_delete=models.CASCADE)
   room_type           = models.ForeignKey(RoomType,on_delete= models.CASCADE)
   agreement_type      = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
   pay_till_date       = models.CharField(max_length=10)
   stamp_duty          = models.BooleanField( choices = CHOICES_BOOLEAN )
   stamp_duty_amt      = models.CharField(max_length=10)
   cost_sheet          = models.CharField(max_length=3)
   cost_sheet_amt      = models.CharField(max_length=7)
   lead_id             = models.ForeignKey(Leads,on_delete=models.CASCADE)
   car_parking_amt     = models.IntegerField()
   car_parking         = models.BooleanField(choices = CHOICES_BOOLEAN)


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
    prop_city           = models.ForeignKey(City,on_delete=models.CASCADE)
    prop_state          = models.ForeignKey(State,on_delete=models.CASCADE)
    prop_in                              = models.ForeignKey(PropertyIn,on_delete=CASCADE)
    cc_available                         = models.BooleanField( choices = CHOICES_BOOLEAN )
    oc_rec                               = models.BooleanField( choices = CHOICES_BOOLEAN )
    oc_rec_floor                         = models.IntegerField()
    municipal_approved                   = models.BooleanField( choices = CHOICES_BOOLEAN )
    area_size                            = models.IntegerField()
    area_in                              = models.ForeignKey(AreaIn,on_delete = models.CASCADE)
    area_type                            = models.ForeignKey(AreaType,on_delete=models.CASCADE)
    room_type                            = models.ForeignKey(RoomType,on_delete= models.CASCADE)
    agreement_type                       = models.ForeignKey(AgreementType,on_delete=models.CASCADE)
    pay_till_date                        = models.CharField(max_length=10)
    previous_aggrement_available         = models.BooleanField(null=True ,blank=True, choices=CHOICES_BOOLEAN)
    registration_done_previous_aggremnet = models.CharField(max_length=100)
    concern_area                         = models.CharField(max_length=100)
    stamp_duty_registration_paid         = models.BooleanField(choices=CHOICES_BOOLEAN)
    stamp_duty_amt                       = models.IntegerField()
    property_tax_paid                    = models.BooleanField(null=True,blank=True,choices = CHOICES_BOOLEAN)
    society_informed                     = models.BooleanField(null=True,blank=True,choices = CHOICES_BOOLEAN)
    car_parking_amt                      = models.IntegerField()
    car_parking                          = models.BooleanField(choices = CHOICES_BOOLEAN)
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
