from LoanClaculator import AgeVerification, LoanCalculation, PropertyVerification
from django.shortcuts import redirect, render
from datetime import date
from .models import *
from account.models import Leads, AdditionalDetails, ContactPerson
from account.models import PropertyDetails, PropType1, PropType2, PropType3
from account.models import PersonalDetails, SalIncomeDetails, SalOtherIncomes, SalAdditionalOtherIncomes, SalCompanyDetails, SalAdditionalDetails, SalExistingCreditCard, SalExistingLoanDetails, Investments
# Create your views here.


def eligibility(request, id):
    lead = Leads.objects.filter(lead_id = id).first()
    add_dets = AdditionalDetails.objects.filter(lead_id = id)     #-> collecting all applicants and co applicants
    banks = Bank.objects.all()
    #-> Dictionaries to collect different data and remarks
    data = {}
    remarks = {}

    for add_det in add_dets:     #-> looping through all applicants as well as co applicants

        #-> setting dictionary to current applicant/co-applicant
        data[add_det.applicant_type] = {}
        remarks[add_det.applicant_type] = {}

        if add_det.cust_type == "Salaried":     #-> calculating for customer type salaried
            banks = Bank.objects.filter(cust_type = "Salaried")

            for bank in banks:
                #-> Setting for each bank
                data[add_det.applicant_type][bank.bank_name] = {}
                remarks[add_det.applicant_type][bank.bank_name] = []

                #-> Checking Property Details which will be only assigned to applicant
                if add_det.applicant_type == "Applicant":
                    prop_det = PropertyDetails.objects.filter(lead_id = id).first()
                    if prop_det.prop_type == "Underconstruction and Buying From Builder" or prop_det.prop_type == "Underconstruction and Buying From Seller" or prop_det.prop_type == "Ready Possession and Buying From Builder":
                        p_type = 1
                        property_type = PropType1.objects.filter(prop_det_id = prop_det.prop_det_id).first()
                    elif prop_det.prop_type == "Resale and Buying From Seller":
                        p_type = 2
                        property_type = PropType2.objects.filter(prop_det_id = prop_det.prop_det_id).first()
                    else:
                        p_type = 3
                        property_type = PropType3.objects.filter(prop_det_id = prop_det.prop_det_id).first()




                    property = PropertyVerification(id, bank)

                    if property.p_type == 3:
                        remarks[add_det.applicant_type][bank.bank_name].append(f"{property.prop_det.prop_type} is not considered by {bank.bank_name}")
                        continue

                    if not property.roomConsiderByBank():
                        remarks[add_det.applicant_type][bank.bank_name].append(f"{bank.bank_name} does not consider {property.property_type.room_type} Room Type")
                        continue

                    if property.p_type == 1:

                        if not property.stageConsiderByBank():
                            remarks[add_det.applicant_type][bank.bank_name].append(f"{bank.bank_name} does not consider {property_type.const_stage} Stage")
                            continue

                        if not property.completionConsiderByBank():
                            remarks[add_det.applicant_type][bank.bank_name].append(f"{bank.bank_name} considers Completion more than {prop.perc_completion}%")
                            continue

                    if property.p_type == 1 or property.p_type == 2:
                        if not property.negativeAreaConsiderByBank():
                            remarks[add_det.applicant_type][bank.bank_name].append(f"{bank.bank_name} does not consider {property_type.prop.loc} Location")
                            continue

                age = Age.objects.filter(bank_id = bank.bank_id).first()
                oth = OtherDetails.objects.filter(bank_id = bank.bank_id).first()
                per_det = PersonalDetails.objects.filter(addi_details_id = add_det.add_det_id).first()
                inc = Income.objects.filter(bank_id = bank.bank_id).first()
                inc_det = SalIncomeDetails.objects.filter(addi_details_id_inc = add_det.add_det_id).first()
                oth_inc = SalOtherIncomes.objects.filter(addi_details_id_other_inc = add_det.add_det_id)
                inc_foir = IncomeFoir.objects.filter(bank_id = bank.bank_id)
                obl = Obligation.objects.filter(bank_id = bank.bank_id).first()
                exi_card = SalExistingCreditCard.objects.filter(add_det_id = add_det.add_det_id)
                exi_loan = SalExistingLoanDetails.objects.filter(add_det_id = add_det.add_det_id)
                oth_roi = OtherDetailsROI.objects.filter(bank_id = bank.bank_id)
                cmp_det = SalCompanyDetails.objects.filter(add_det_id = add_det.add_det_id).first()


                #-> Checking minimum age
                if AgeVerification.minAge(per_det, age):
                    data[add_det.applicant_type][bank.bank_name] = 0
                    remarks[add_det.applicant_type][bank.bank_name].append(f"Age of applicant should be greater than {age.min_age}")
                    continue

                #-> Checking Nationality
                if per_det.nationality == "Non Resident Indian":
                    remarks[add_det.applicant_type][bank.bank_name].append(f"Nationality Should be Resident")
                    continue

                #-> Retire age
                retire_age, remark = AgeVerification.retireAge(per_det, age, cmp_det, bank, add_det)
                remarks[add_det.applicant_type][bank.bank_name].append(remark)

                #-> Tenure
                tenure = LoanCalculation.calcTenure(retire_age, per_det.age, oth.tenure)
                data[add_det.applicant_type][bank.bank_name]['tenure'] = tenure

                #-> Income calculations

                net_salary = 0
                gross_salary = 0
                incentives = LoanCalculation.calcIncentives(inc.incentive, inc_det.incentivesType, inc_det.incentive_amt, inc.bonus_avg_yearly_percent, inc.bonus_avg_half_yearly_percent, inc.bonus_avg_qtr_percent, inc.incen_percent)
                bonus = LoanCalculation.calcBonus(inc_det.bonusType, inc.bonus, inc_det.bonus_amt, inc.bonus_avg_yearly_percent, inc.bonus_avg_half_yearly_percent, inc.bonus_avg_qtr_percent, inc.incen_percent)
                rental_income = LoanCalculation.clacRentalIncome(inc.rent_income, inc.rent_agreement_type, oth_inc, inc.rent_ref_in_bank, inc.rent_inc_percent)
                total_bns_inc_rent = 0

                if inc.net_sal != "N":
                    net_salary = int(inc_det.net_sal)
                if inc.gross_sal != "N":
                    gross_salary = int(inc_det.gross_sal)

                #-> obligation
                obligation = LoanCalculation.calcObligation(obl.emi_oblig, obl.credit_card, exi_loan, exi_card, obl.emi_oblig_not_consi, obl.credit_card_oblig_percent)
                data[add_det.applicant_type][bank.bank_name]['obligation'] = obligation

                #-> Total extra income
                total_bns_inc_rent = bonus + incentives + rental_income

                #-> Income FOIR
                income = 0
                if gross_salary == 0:
                    income = net_salary
                else:
                    income = gross_salary
                total_income = income + total_bns_inc_rent
                data[add_det.applicant_type][bank.bank_name]['total_income'] = total_income
                foir_percent, income_foir = LoanCalculation.calcIncomeFOIR(total_income, inc_foir)
                data[add_det.applicant_type][bank.bank_name]['foir_per'] = foir_percent
                data[add_det.applicant_type][bank.bank_name]['inc_foir'] = income_foir

                #-> Rate Of Interest
                roi = LoanCalculation.calcROI(oth.prevailing_rate, per_det.cibil_score, oth_roi, per_det.gender, int(per_det.loan_amt), per_det.cibil_type)
                if roi == -1:
                    remarks[add_det.applicant_type][bank.bank_name].append(f"Your CIBIL Score is too low for approval of loan")
                    continue
                data[add_det.applicant_type][bank.bank_name]['roi'] = roi

                #-> Per Lac Emi
                per_lac_emi = LoanCalculation.calcPerLacEMI(roi, tenure)
                data[add_det.applicant_type][bank.bank_name]['per_lac_emi'] = per_lac_emi

                #-> Loan eligibility
                loan_eligibility = (income_foir - obligation)/per_lac_emi
                data[add_det.applicant_type][bank.bank_name]['loan_eligibility'] = loan_eligibility

    #-> Calculating total eligibility of applicants for each bank
    ttl_eli = {}
    p_l_emi = {}
    for bank in banks:
        total_eli = 0
        for key in data.keys():
            if bank.bank_name in data[key].keys():
                if 'loan_eligibility' in data[key][bank.bank_name].keys():
                    total_eli += data[key][bank.bank_name]['loan_eligibility']
                # if 'per_lac_emi' in data[key][bank.bank_name].keys():
                #     p_l_emi[bank.bank_name] = data[key][bank.bank_name]['per_lac_emi']
        ttl_eli[bank.bank_name] = total_eli

    #-> Loan towards valuation
    add_det2 = AdditionalDetails.objects.filter(lead_id = id, applicant_type="Applicant").first()
    app_det = PersonalDetails.objects.filter(addi_details_id = add_det2.add_det_id).first()
    agreement_value = int(property.property_type.agreement_val)
    market_value = int(property.property_type.market_val)
    loan_req = int(app_det.loan_amt)
    bank_eli = 0
    loan = 0
    loan_approved = {}


    for bank in banks:
        if loan_req < ttl_eli[bank.bank_name]*100000:
            loan = loan_req
        else:
            loan = ttl_eli[bank.bank_name]*100000

        if p_type == 1:
            ltv = LoanTowardsValuation.objects.filter(bank_id = bank.bank_id)
            bank_eli = LoanCalculation.calcUnderconstructionLTV(agreement_value, ltv)
        if p_type == 2:
            stp_amt = property.property_type.stp_amt
            reg_amt = property.property_type.reg_amt
            ltv = LtvResale.objects.filter(bank_id = bank.bank_id)
            bank_eli = LoanCalculation.calcResaleLTV(market_value, agreement_value, stp_amt, reg_amt, ltv)
        print(bank_eli)
        if bank_eli < loan:
            loan = bank_eli
        loan_approved[bank.bank_name] = round(loan,2)

        for app in data.keys():
            if bank.bank_name in data[app].keys():
                if 'per_lac_emi' in data[key][bank.bank_name].keys():
                    data[app][bank.bank_name]['emi'] = round((loan_approved[bank.bank_name]/100000)*data[app][bank.bank_name]['per_lac_emi'],2)


    display = {}
    for app in data.keys():
        display[app] = {}
        for bank in banks:
            display[app][bank.bank_name] = {}
            if bank.bank_name in data[app].keys():
                if 'tenure' in data[app][bank.bank_name]:
                    display[app][bank.bank_name]['tenure'] = data[app][bank.bank_name]['tenure']
                if 'total_income' in data[app][bank.bank_name]:
                    display[app][bank.bank_name]['total_income'] = round(data[app][bank.bank_name]['total_income'],2)
                if 'loan_eligibility' in data[app][bank.bank_name]:
                    display[app][bank.bank_name]['loan_eligibility'] = round(data[app][bank.bank_name]['loan_eligibility']*100000,2)
                if 'roi' in data[app][bank.bank_name]:
                    display[app][bank.bank_name]['roi'] = data[app][bank.bank_name]['roi']
                if 'per_lac_emi' in data[app][bank.bank_name]:
                    display[app][bank.bank_name]['per_lac_emi'] = round(data[app][bank.bank_name]['per_lac_emi'],2)

    total_emi = {}
    for bank in banks:
        total_emi[bank.bank_name] = 0
        for app in data.keys():
            if 'emi' in data[app][bank.bank_name]:
                total_emi[bank.bank_name] += data[app][bank.bank_name]['emi']
    return render(request, "HomeLoan/eligibility.html", {'remarks':remarks, 'display':display , 'loan_approved':loan_approved, 'total_emi':total_emi})


def PPAge(request, ppid):
    if request.method == 'POST':
        min_age = int(request.POST['min_age'])
        retire_age = int(request.POST['retire_age'])
        max_age_consi_others = int(request.POST['max_age_consi_others'])
        max_age_consi_gov = int(request.POST['max_age_consi_gov'])
        bank = Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]

        age = Age(min_age=min_age, retire_age=retire_age, max_age_consi_others=max_age_consi_others, max_age_consi_gov=max_age_consi_gov, bank_id=bank)
        age.save()
        return redirect('editproductandpolicy', id=ppid)

    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/age.html', context=context)

def PPeditAge(request, ppid, ageid):
    if request.method == 'POST':
        Age.objects.filter(age_id=ageid).update(
            min_age = int(request.POST['min_age']),
            retire_age = int(request.POST['retire_age']),
            max_age_consi_others = int(request.POST['max_age_consi_others']),
            max_age_consi_gov = int(request.POST['max_age_consi_gov'])
        )
        return redirect('editproductandpolicy', id=ppid)
    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'age': Age.objects.filter(age_id=ageid)[0]
    }
    return render(request, 'HomeLoan/editage.html', context=context)

def PPnegativearea(request, ppid):
    if request.method == 'POST':
        neg_area = request.POST['neg_area']
        bank = Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]

        negativearea = NegativeArea(neg_area=neg_area, bank_id=bank)
        negativearea.save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/negativearea.html', context=context)

def PPeditNegativearea(request, ppid, negativeareaid):
    if request.method == 'POST':
        NegativeArea.objects.filter(neg_area_id=negativeareaid).update(
            neg_area = request.POST['neg_area']
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'negativearea': NegativeArea.objects.filter(neg_area_id=negativeareaid)[0]
    }
    return render(request, 'HomeLoan/editnegativearea.html', context=context)

def PPbank(request):
    if request.method == 'POST':
        bank_name = request.POST['bank_name']
        cust_type = request.POST['cust_type']
        bank = Bank(bank_name=bank_name, cust_type=cust_type)
        bank.save()
        return redirect('AddProductsAndPolicy')

def PPnegativeemployerprofile(request, ppid):
    if request.method == 'POST':
        neg_emp_pro = request.POST['neg_emp_pro']
        bank = Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]

        NegativeEmployerProfile(neg_emp_pro=neg_emp_pro, bank_id=bank).save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/negativeemployerprofile.html', context=context)

def PPeditnegativeemployerprofile(request, ppid, negativeemployerprofileid):
    if request.method == 'POST':
        NegativeEmployerProfile.objects.filter(neg_emp_pro_id=negativeemployerprofileid).update(
            neg_emp_pro = request.POST['neg_emp_pro']
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'negativeemployerprofile': NegativeEmployerProfile.objects.filter(neg_emp_pro_id=negativeemployerprofileid)[0]
    }
    return render(request, 'HomeLoan/editnegativeemployerprofile.html', context=context)

def PPCibil(request, ppid):
    if request.method == 'POST':
        cibil_range_min = int(request.POST['cibil_range_min'])
        cibil_range_max = int(request.POST['cibil_range_max'])
        bank = Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]

        Cibil(cibil_range_min=cibil_range_min, cibil_range_max=cibil_range_max, bank_id=bank).save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/Cibil.html', context=context)

def PPeditCibil(request, ppid, cibilid):
    if request.method == 'POST':
        Cibil.objects.filter(cibil_id=cibilid).update(
            cibil_range_min = request.POST['cibil_range_min'],
            cibil_range_max = request.POST['cibil_range_max']
        )
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'cibil': Cibil.objects.filter(cibil_id=cibilid)[0]
    }
    return render(request, 'HomeLoan/editCibil.html', context=context)


def PPobligation(request, ppid):
    if request.method == 'POST':
        Obligation(
            emi_oblig=request.POST['emi_oblig'],
            emi_oblig_not_consi=request.POST['emi_oblig_not_consi'],
            credit_card=request.POST['credit_card'],
            credit_card_oblig_percent=int(request.POST['credit_card_oblig_percent']),
            gold_loan=request.POST['gold_loan'],
            gold_loan_percent=int(request.POST['gold_loan_percent']),
            bank_id = Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/obligation.html', context=context)

def PPeditobligation(request, ppid, obligationid):
    if request.method == 'POST':
        Obligation.objects.filter(obligation_id=obligationid).update(
            emi_oblig=request.POST['emi_oblig'],
            emi_oblig_not_consi=request.POST['emi_oblig_not_consi'],
            credit_card=request.POST['credit_card'],
            credit_card_oblig_percent=int(request.POST['credit_card_oblig_percent']),
            gold_loan=request.POST['gold_loan'],
            gold_loan_percent=int(request.POST['gold_loan_percent']),
        )
        return redirect('editproductandpolicy', ppid)

    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'pp': ProductsAndPolicy.objects.filter(prod_id=ppid)[0],
        'obligation': Obligation.objects.filter(obligation_id=obligationid)[0],
    }
    return render(request, 'HomeLoan/editobligation.html', context=context)

def PPcompany(request, ppid):
    if request.method == 'POST':
        comp_type = request.POST['comp_type']
        bank = Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]

        Company(comp_type=comp_type, bank_id=bank).save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/company.html', context=context)

def PPeditcompany(request, ppid, companyid):
    if request.method == 'POST':
        Company.objects.filter(comp_id=companyid).update(
            comp_type = request.POST['comp_type']
        )
        return redirect('editproductandpolicy', ppid)
    context={
        'company': Company.objects.filter(comp_id=companyid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editcompany.html', context=context)

def PPOtherDetailsRoi(request, ppid):
    if request.method == 'POST':
        min_loan_amt = int(request.POST['min_loan_amt'])
        max_loan_amt = int(request.POST['max_loan_amt'])
        min_val = int(request.POST['min_val'])
        max_val = int(request.POST['max_val'])
        roi_men = request.POST['roi_men']
        roi_women = request.POST['roi_women']
        bank = Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]

        OtherDetailsROI(
            min_loan_amt=min_loan_amt,
            max_loan_amt=max_loan_amt,
            min_val=min_val,
            max_val=max_val,
            roi_men=roi_men,
            roi_women=roi_women,
            bank_id=bank
        ).save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/OtherDetailsRoi.html', context=context)

def PPeditotherdetailsroi(request, ppid, otherdetailsroiid):
    if request.method == 'POST':
        OtherDetailsROI.objects.filter(oth_det_roi_id=otherdetailsroiid).update(
            min_loan_amt = int(request.POST['min_loan_amt']),
            max_loan_amt = int(request.POST['max_loan_amt']),
            min_val = int(request.POST['min_val']),
            max_val = int(request.POST['max_val']),
            roi_men = request.POST['roi_men'],
            roi_women = request.POST['roi_women']
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'otherdetailsroi': OtherDetailsROI.objects.filter(oth_det_roi_id=otherdetailsroiid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editotherdetailsroi.html', context=context)

def PPcostsheet(request, ppid):
    if request.method == 'POST':
        particulars = request.POST.get('particulars')

        CostSheet(particulars=particulars).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/costsheet.html', context=context)

def PPeditcostsheet(request, ppid, costsheetid):
    if request.method == 'POST':
        CostSheet.objects.filter(cost_particular_id=costsheetid).update(
            particulars = request.POST['particulars']
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'costsheet': CostSheet.objects.filter(cost_particular_id=costsheetid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editcostsheet.html', context=context)

def PPProducts(request):
    if request.method == 'POST':
        product = request.POST['prod_name']
        bank = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]

        Products(prod_name=product, bank_id=bank).save()
        return redirect('dashboard')
    context={
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/Products.html', context=context)

def PPcustomerdesignation(request, ppid):
    if request.method == 'POST':
        cust_desig = request.POST['cust_desig']

        CustomerDesignation(cust_desig=cust_desig, bank_id=Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/customerdesignation.html', context=context)

def ppeditcustomerdesignation(request, ppid, customerdesignationid):
    if request.method== 'POST':
        CustomerDesignation.objects.filter(cust_desig_id=customerdesignationid).update(
            cust_desig=request.POST['cust_desig'],
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'customerdesignation': CustomerDesignation.objects.filter(cust_desig_id=customerdesignationid)[0]
    }
    return render(request, 'HomeLoan/editcustomerdesignation.html', context=context)

def PPProperty(request, ppid):
    if request.method == 'POST':
        Property(
            builder_cat=request.POST['builder_cat'],
            occupation_certi = request.POST['occupation_certi'],
            prev_agreement = request.POST['prev_agreement'],
            sub_scheme = request.POST['sub_scheme'],
            perc_completion = int(request.POST['perc_completion']),
            bank_id=Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)

    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/Property.html', context=context)

def PPeditproperty(request, ppid, propertyid):
    if request.method == 'POST':
        property = Property.objects.filter(prop_id=propertyid)
        property.update(
            builder_cat=request.POST['builder_cat'],
            occupation_certi = request.POST['occupation_certi'],
            prev_agreement = request.POST['prev_agreement'],
            sub_scheme = request.POST['sub_scheme'],
            perc_completion = int(request.POST['perc_completion']),
        )
        return redirect('editproductandpolicy', ppid)
    context =  {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'pp': ProductsAndPolicy.objects.filter(prod_id=ppid)[0],
        'property': Property.objects.filter(prop_id=propertyid)[0]
    }
    return render(request, 'HomeLoan/editproperty.html', context)


def PPcustomer(request, ppid):
    if request.method == 'POST':
        Customer(
            min_age = int(request.POST['min_age']),
            total_Exp = int(request.POST['total_Exp']),
            form16 = request.POST['form16'],
            salary_type = request.POST['salary_type'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/customer.html', context=context)

def PPeditcustomer(request, ppid, customerid):
    if request.method == 'POST':
        Customer.objects.filter(cust_id=customerid).update(
            min_age = int(request.POST['min_age']),
            total_Exp = int(request.POST['total_Exp']),
            form16 = request.POST['form16'],
            salary_type = request.POST['salary_type'],
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'customer': Customer.objects.filter(cust_id=customerid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editcustomer.html', context=context)

def PPPropertyType(request, ppid):
    if request.method == 'POST':
        PropertyType(
            prop_type = request.POST['prop_type'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/PropertyType.html', context=context)

def PPeditPropertyType(request, ppid, propertytypeid):
    if request.method == 'POST':
        PropertyType.objects.filter(prop_type_id=propertytypeid).update(
            prop_type = request.POST['prop_type'],
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'propertytype': PropertyType.objects.filter(prop_type_id=propertytypeid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editpropertytype.html', context=context)

def PPcustomernationality(request, ppid):
    if request.method == 'POST':
        CustomerNationality(
            cust_nat = request.POST['cust_nat'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', id=ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/customernationality.html', context=context)

def PPeditcustomernationality(request, ppid, customernationalityid):
    if request.method == 'POST':
        CustomerNationality.objects.filter(cust_nat_id=customernationalityid).update(
            cust_nat = request.POST['cust_nat']
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'customernatnality': CustomerNationality.objects.filter(cust_nat_id=customernationalityid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editcustomernationality.html', context=context)

def PPfees(request, ppid):
    if request.method == 'POST':
        Fees(
            login_fees = request.POST['login_fees'],
            proc_fee_app = request.POST['proc_fee_app'],
            proc_fee_type = request.POST['proc_fee_type'],
            proc_fee_flat_loan_amtwise = request.POST['proc_fee_flat_loan_amtwise'],
            proc_fee_percent_loan_amtwise = request.POST['proc_fee_percent_loan_amtwise'],
            offers = request.POST['offers'],
            offline_or_online = request.POST['offline_or_online'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/fees.html', context=context)

def PPeditfee(request, ppid, feeid):
    if request.method == 'POST':
        Fees.objects.filter(fee_id=feeid).update(
            login_fees = request.POST['login_fees'],
            proc_fee_app = request.POST['proc_fee_app'],
            proc_fee_type = request.POST['proc_fee_type'],
            proc_fee_flat_loan_amtwise = request.POST['proc_fee_flat_loan_amtwise'],
            proc_fee_percent_loan_amtwise = request.POST['proc_fee_percent_loan_amtwise'],
            offers = request.POST['offers'],
            offline_or_online = request.POST['offline_or_online'],
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'fee': Fees.objects.filter(fee_id=feeid)[0]
    }
    return render(request, 'HomeLoan/editfee.html', context=context)

def PPRemarks(request, ppid):
    if request.method == 'POST':
        Remarks(
            remark = request.POST['Remarks']
        ).save()
        return redirect('dashboard')
    context={}
    return render(request, 'HomeLoan/Remarks.html', context=context)

def PPincomefoir(request, ppid):
    if request.method == 'POST':
        IncomeFoir(
            min_amt = int(request.POST['min_amt']),
            max_amt = int(request.POST['max_amt']),
            percent = int(request.POST['percent']),
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/incomefoir.html', context=context)

def PPeditincomefoir(request, ppid, incomefoirid):
    if request.method == 'POST':
        IncomeFoir.objects.filter(inc_foir_id=incomefoirid).update(
            min_amt = int(request.POST['min_amt']),
            max_amt = int(request.POST['max_amt']),
            percent = int(request.POST['percent']),

        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'incomefoir': IncomeFoir.objects.filter(inc_foir_id=incomefoirid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editincomefoir.html', context=context)

def PPRoomType(request, ppid):
    if request.method == 'POST':
        RoomType(
            room_type = request.POST['room_type'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/RoomType.html', context=context)

def PPediRoomType(request, ppid, roomtypeid):
    if request.method == 'POST':
        RoomType.objects.filter(romm_id=roomtypeid).update(
            room_type = request.POST['room_type']
        )
        return redirect('editproductandpolicy', ppid)
        context = {
            'roomtype': RoomType.objects.filter(romm_id=roomtypeid)[0],
            'product': Products.objects.filter(prod_id=ppid)[0],
        }
        return redirect(request, 'HomeLoan/editroomtype.html', context=context)
    context = {
        'roomtype': RoomType.objects.filter(romm_id=roomtypeid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editroomtype.html', context=context)

def PPincome(request, ppid):
    if request.method == 'POST':
        Income(
            gross_sal = request.POST['gross_sal'],
            net_sal = request.POST['net_sal'],
            bonus = request.POST['bonus'],
            bonus_avg_yearly = request.POST['bonus_avg_yearly'],
            bonus_avg_yearly_percent = request.POST['bonus_avg_yearly_percent'],
            bonus_avg_qtr = request.POST['bonus_avg_qtr'],
            bonus_avg_qtr_percent = request.POST['bonus_avg_qtr_percent'],
            bonus_avg_half_yearly = request.POST['bonus_avg_half_yearly'],
            bonus_avg_half_yearly_percent = request.POST['bonus_avg_half_yearly_percent'],
            rent_income = request.POST['rent_income'],
            rent_agreement_type = request.POST['rent_agreement_type'],
            bank_ref = request.POST['bank_ref'],
            rent_ref_in_bank = request.POST['rent_ref_in_bank'],
            rent_inc_percent = request.POST['rent_inc_percent'],
            fut_rent = request.POST['fut_rent'],
            fut_rent_percent = request.POST['fut_rent_percent'],
            incentive = request.POST['incentive'],
            incen_avg_months = request.POST['incen_avg_months'],
            incen_percent = request.POST['incen_percent'],
            coApplicant_No_Income_only_Rent_income = request.POST['coApplicant_No_Income_only_Rent_income'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/income.html', context=context)

def PPeditincome(request, ppid, incomeid):
    if request.method == 'POST':
        Income.objects.filter(income_id=incomeid).update(
            gross_sal = request.POST['gross_sal'],
            net_sal = request.POST['net_sal'],
            bonus = request.POST['bonus'],
            bonus_avg_yearly = request.POST['bonus_avg_yearly'],
            bonus_avg_yearly_percent = request.POST['bonus_avg_yearly_percent'],
            bonus_avg_qtr = request.POST['bonus_avg_qtr'],
            bonus_avg_qtr_percent = request.POST['bonus_avg_qtr_percent'],
            bonus_avg_half_yearly = request.POST['bonus_avg_half_yearly'],
            bonus_avg_half_yearly_percent = request.POST['bonus_avg_half_yearly_percent'],
            rent_income = request.POST['rent_income'],
            rent_agreement_type = request.POST['rent_agreement_type'],
            bank_ref = request.POST['bank_ref'],
            rent_ref_in_bank = request.POST['rent_ref_in_bank'],
            rent_inc_percent = request.POST['rent_inc_percent'],
            fut_rent = request.POST['fut_rent'],
            fut_rent_percent = request.POST['fut_rent_percent'],
            incentive = request.POST['incentive'],
            incen_avg_months = request.POST['incen_avg_months'],
            incen_percent = request.POST['incen_percent'],
            coApplicant_No_Income_only_Rent_income = request.POST['coApplicant_No_Income_only_Rent_income'],
        )
        return redirect('editproductandpolicy', ppid)

    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'income': Income.objects.filter(income_id=incomeid)[0]
    }
    return render(request, 'HomeLoan/editincome.html', context=context)

def PPStageOfConstruction(request, ppid):
    if request.method == 'POST':
        StageOfConstruction(
            stage = request.POST['stage'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('dashboard')
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/StageOfConstruction.html', context=context)

def PPeditstageofconstruction(request, ppid, stageofconstructionid):
    if request.method == 'POST':
        StageOfConstruction.objects.filter(stage_id=stageofconstructionid).update(
            stage = request.POST['stage'],
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'stageofconstruction': StageOfConstruction.objects.filter(stage_id=stageofconstructionid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editstageofconstruction.html', context=context)

def PPLoanAmount(request, ppid):
    if request.method == 'POST':
        LoanAmount(
            min_loan_amt = int(request.POST['min_loan_amt']),
            max_loan_amt = int(request.POST['max_loan_amt']),
            total_Exp = int(request.POST['total_Exp']),
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/LoanAmount.html', context=context)

def PPeditLoanAmount(request, ppid, loanamountid):
    if request.method == 'POST':
        LoanAmount.objects.filter(loan_id=loanamountid).update(
            min_loan_amt = int(request.POST['min_loan_amt']),
            max_loan_amt = int(request.POST['max_loan_amt']),
            total_Exp = int(request.POST['total_Exp'])
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'loanamount': LoanAmount.objects.filter(loan_id=loanamountid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editloanamount.html', context=context)

def PPLtvResale(request, ppid):
    if request.method == 'POST':
        LtvResale(
            min_amount = request.POST['min_amount'],
            max_amount = request.POST['max_amount'],
            rbi_guidelines = request.POST['rbi_guidelines'],
            doccument_cost = request.POST['doccument_cost'],
            additional = request.POST['additional'],
            car_parking = request.POST['car_parking'],
            total = request.POST['total'],
            market_value = request.POST['market_value'],
            av_capping = request.POST['av_capping'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/LtvResale.html', context=context)

def PPeditLtvResale(request, ppid, ltvresaleid):
    if request.method == 'POST':
        LtvResale.objects.filter(ltv_id=ltvresaleid).update(
            min_amount = request.POST['min_amount'],
            max_amount = request.POST['max_amount'],
            rbi_guidelines = request.POST['rbi_guidelines'],
            doccument_cost = request.POST['doccument_cost'],
            additional = request.POST['additional'],
            car_parking = request.POST['car_parking'],
            total = request.POST['total'],
            market_value = request.POST['market_value'],
            av_capping = request.POST['av_capping']
        )
        return redirect('editproductandpolicy', ppid)
    context = {
        'ltvresale': LtvResale.objects.filter(ltv_id=ltvresaleid)[0],
        'product': Products.objects.filter(prod_id=ppid)[0],
    }
    return render(request, 'HomeLoan/editltvresale.html', context=context)

def PPLoantowardsvaluation(request, ppid):
    if request.method == 'POST':
        LoanTowardsValuation(
            cost_sheet = request.POST['cost_sheet'],
            min_amount = int(request.POST['min_amount']),
            max_amount = int(request.POST['max_amount']),
            rbi_guidelines = request.POST['rbi_guidelines'],
            ammenity = request.POST['ammenity'],
            additional = request.POST['additional'],
            car_parking = request.POST['car_parking'],
            car_parking_percent = request.POST['car_parking_percent'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)
    context={
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/Loantowardsvaluation.html', context=context)



def PPeditloantowardsvalution(request, ppid, ltvid):
    if request.method == 'POST':
        LoanTowardsValuation.objects.filter(loan_tow_val_id=ltvid).update(
            cost_sheet = request.POST['cost_sheet'],
            min_amount = int(request.POST['min_amount']),
            max_amount = int(request.POST['max_amount']),
            rbi_guidelines = request.POST['rbi_guidelines'],
            ammenity = request.POST['ammenity'],
            additional = request.POST['additional'],
            car_parking = request.POST['car_parking'],
            car_parking_percent = request.POST['car_parking_percent'],
        )

        return redirect('editproductandpolicy', ppid)

    context={
        'ltv': LoanTowardsValuation.objects.filter(loan_tow_val_id=ltvid)[0],
        'pp' : ProductsAndPolicy.objects.filter(prod_id=ppid)[0]
    }
    return render(request, 'HomeLoan/editloantowardsvalution.html', context=context)

def PPotherdetails(request, ppid):
    if request.method == 'POST':
        OtherDetails(
            prevailing_rate = request.POST['prevailingrate'],
            tenure = request.POST['tenure'],
            inward_cheque_return = request.POST['inwardchequereturn'],
            multiple_inquiry = request.POST['multipleinquiry'],
            bank_id= Bank.objects.filter(bank_id=Products.objects.filter(prod_id=ppid)[0].bank_id.bank_id)[0]
        ).save()
        return redirect('editproductandpolicy', ppid)

    context = {
        'product': Products.objects.filter(prod_id=ppid)[0],
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/otherdetails.html', context=context)

def ppeditotherdetail(request, ppid, otherdetailid):
    if request.method == 'POST':
        OtherDetails.objects.filter(oth_det_id=otherdetailid).update(
            prevailing_rate = request.POST['prevailingrate'],
            tenure = request.POST['tenure'],
            inward_cheque_return = request.POST['inwardchequereturn'],
            multiple_inquiry = request.POST['multipleinquiry'],
        )
        return redirect('editproductandpolicy', ppid)

    context = {
        'pp': ProductsAndPolicy.objects.filter(prod_id=ppid)[0],
        'otherdetail': OtherDetails.objects.filter(oth_det_id=otherdetailid)[0]
    }
    return render(request, 'HomeLoan/editotherdetails.html', context=context)

def AddProductsAndPolicy(request):
    if request.method == 'POST':
        product = Products(
            prod_name = request.POST['productname'],
            bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
        )
        product.save()
        if request.POST['min_age'] != '':
            Age(
                min_age = int(request.POST['min_age']),
                retire_age = int(request.POST['retire_age']),
                max_age_consi_others = int(request.POST['Max_age_consi_others']),
                max_age_consi_gov = int(request.POST['Max_age_consi_others']),
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

        if request.POST['cibil_range_min'] != '':
            Cibil(
                cibil_range_min = int(request.POST['cibil_range_min']),
                cibil_range_max = int(request.POST['cibil_range_max']),
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

        if request.POST['comp_type'] != '':
            Company(
                comp_type = request.POST['comp_type'],
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

        if request.POST['min_age'] != '':
            Customer(
                min_age = int(request.POST['min_age']),
                total_Exp = int(request.POST['total_exp']),
                form16 = request.POST['form16'],
                salary_type = request.POST['salary_type'],
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

        if request.POST['cust_desig'] != '':
            CustomerDesignation(
                cust_desig = request.POST['cust_desig'],
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

        if request.POST['cust_nat'] != '':
            CustomerNationality(
                cust_nat = request.POST['cust_nat'],
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

        if request.POST['loginfees'] != '':
            Fees(
                login_fees = request.POST['loginfees'],
                proc_fee_app = request.POST['procfeeapp'],
                proc_fee_type = request.POST['procfeetype'],
                proc_fee_flat_loan_amtwise = request.POST['procfeeflatloanamtwise'],
                proc_fee_percent_loan_amtwise = request.POST['procfeepercentloanamtwise'],
                offers = request.POST['offers'],
                offline_or_online = request.POST['offlineonline'],
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

        if request.POST['grosssal'] != '':
            Income(
                gross_sal = request.POST['grosssal'],
                net_sal = request.POST['netsal'],
                bonus = request.POST['bonus'],
                bonus_avg_yearly = request.POST['bonus_avg_yearly'],
                bonus_avg_yearly_percent = request.POST['bonus_avg_yearly_percent'],
                bonus_avg_qtr = request.POST['bonus_avg_qtr'],
                bonus_avg_qtr_percent = request.POST['bonus_avg_qtr_percent'],
                bonus_avg_half_yearly = request.POST['bonus_avg_half_yearly'],
                bonus_avg_half_yearly_percent = request.POST['bonus_avg_half_yearly_percent'],
                rent_income = request.POST['rent_income'],
                rent_agreement_type = request.POST['rentagreementtype'],
                bank_ref = request.POST['bank_ref'],
                rent_ref_in_bank = request.POST['rent_ref_in_bank'],
                rent_inc_percent = request.POST['rent_inc_percent'],
                fut_rent = request.POST['fut_rent'],
                fut_rent_percent = request.POST['fut_rent_percent'],
                incentive = request.POST['incentive'],
                incen_avg_months = request.POST['incen_avg_months'],
                incen_percent = request.POST['incen_percent'],
                coApplicant_No_Income_only_Rent_income = request.POST['coApplicant_No_Income_only_Rent_income'],
                bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
            ).save()

            if request.POST['min_amt'] != '':
                IncomeFoir(
                    min_amt = int(request.POST['min_amt']),
                    max_amt = int(request.POST['max_amt']),
                    percent = int(request.POST['percent']),
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['min_loan_amt'] != '':
                LoanAmount(
                    min_loan_amt = int(request.POST['min_loan_amt']),
                    max_loan_amt = int(request.POST['max_loan_amt']),
                    total_Exp = int(request.POST['total_exp']),
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['cost_sheet'] != '':
                LoanTowardsValuation(
                    cost_sheet = request.POST['cost_sheet'],
                    min_amount = int(request.POST['min_amount']),
                    max_amount = int(request.POST['max_amount']),
                    rbi_guidelines = request.POST['rbi_guideline'],
                    ammenity = request.POST['ammenity'],
                    additional = request.POST['additional'],
                    car_parking = request.POST['car_parking'],
                    car_parking_percent = request.POST['car_parking_parcent'],
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['min_amount'] != '':
                LtvResale(
                    min_amount = int(request.POST['min_amount']),
                    max_amount = int(request.POST['max_amount']),
                    rbi_guidelines = int(request.POST['ltvrbi_guideline']),
                    doccument_cost = int(request.POST['doccument_cost']),
                    additional = int(request.POST['additional']),
                    car_parking = int(request.POST['car_parking']),
                    total = int(request.POST['total']),
                    market_value = int(request.POST['market_value']),
                    av_capping = int(request.POST['av_capping']),
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['neg_emp_pro'] != '':
                NegativeEmployerProfile(
                    neg_emp_pro = request.POST['neg_emp_pro'],
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['neg_area'] != '':
                NegativeArea(
                    neg_area = request.POST['neg_area'],
                    bank_id  = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['emioblig'] != '':
                Obligation(
                    emi_oblig = request.POST['emioblig'],
                    emi_oblig_not_consi = request.POST['emioblignotconsidered'],
                    credit_card = request.POST['creditcard'],
                    credit_card_oblig_percent = int(request.POST['creditcardobligperc']),
                    gold_loan = request.POST['goldloan'],
                    gold_loan_percent = int(request.POST['goldloanpercent']),
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['prevailingrate'] != '':
                OtherDetails(
                    prevailing_rate = int(request.POST['prevailingrate']),
                    tenure = request.POST['tenur'],
                    inward_cheque_return = request.POST['inwardchequereturn'],
                    multiple_inquiry = request.POST['multipleinquiry'],
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['min_loan_amt'] != '':
                OtherDetailsROI(
                    min_loan_amt = int(request.POST['min_loan_amt']),
                    max_loan_amt = int(request.POST['max_loan_amt']),
                    min_val = int(request.POST['min_val']),
                    max_val = int(request.POST['max_val']),
                    roi_women = request.POST['roi_women'],
                    roi_men = request.POST['roi_men'],
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['buildercategory'] != '':
                Property(
                    builder_cat = request.POST['buildercategory'],
                    occupation_certi = request.POST['occupationcerti'],
                    prev_agreement = request.POST['previousagreement'],
                    sub_scheme = request.POST['subscheme'],
                    perc_completion = int(request.POST['perccompletion']),
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['prop_type'] != '':
                PropertyType(
                    prop_type = request.POST['prop_type'],
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['room_type'] != '':
                RoomType(
                    room_type = request.POST['room_type'],
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()

            if request.POST['stage'] != '':
                StageOfConstruction(
                    stage = request.POST['stage'],
                    bank_id = Bank.objects.filter(bank_id=int(request.POST['bank']))[0]
                ).save()


        return redirect('editproductandpolicy', id=product.prod_id)

    context = {
        'banks': Bank.objects.all(),
    }
    return render(request, 'HomeLoan/AddProductsAndPolicy.html', context=context)


def listproductandpolicy(request):
    context = {
        'Products': Products.objects.all()
    }
    return render(request, 'HomeLoan/listproductsandpolicy.html', context=context)

def editproductandpolicy(request, id):
    product = Products.objects.filter(prod_id=id)[0]
    context =  {
        'product': product,
        'ages': Age.objects.filter(bank_id=product.bank_id),
        'cibils': Cibil.objects.filter(bank_id=product.bank_id),
        'companys': Company.objects.filter(bank_id=product.bank_id),
        'costsheets': CostSheet.objects.all(),
        'customers': Customer.objects.filter(bank_id=product.bank_id),
        'customerdesinations': CustomerDesignation.objects.filter(bank_id=product.bank_id),
        'customernationalities': CustomerNationality.objects.filter(bank_id=product.bank_id),
        'fees': Fees.objects.filter(bank_id=product.bank_id),
        'incomes': Income.objects.filter(bank_id=product.bank_id),
        'incomefoirs': IncomeFoir.objects.filter(bank_id=product.bank_id),
        'loanamounts': LoanAmount.objects.filter(bank_id=product.bank_id),
        'loantowardsvalutions': LoanTowardsValuation.objects.filter(bank_id=product.bank_id),
        'ltvresales': LtvResale.objects.filter(bank_id=product.bank_id),
        'negativeemployerprofiles': NegativeEmployerProfile.objects.filter(bank_id=product.bank_id),
        'negativeareas': NegativeArea.objects.filter(bank_id=product.bank_id),
        'obligations': Obligation.objects.filter(bank_id=product.bank_id),
        'otherdetails': OtherDetails.objects.filter(bank_id=product.bank_id),
        'otherdetailsrois': OtherDetailsROI.objects.filter(bank_id=product.bank_id),
        'properties': Property.objects.filter(bank_id=product.bank_id),
        'propertytypes': PropertyType.objects.filter(bank_id=product.bank_id),
        'roomtypes': RoomType.objects.filter(bank_id=product.bank_id),
        'stageofconstructions': StageOfConstruction.objects.filter(bank_id=product.bank_id),
    }
    return render(request, 'HomeLoan/editproductandpolicy.html', context=context)

