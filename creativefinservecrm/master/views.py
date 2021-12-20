from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def Agreementtype_form(request):
    if request.method == 'POST':
        agreementtypeformvalue = request.POST['AgreementType'].strip()
        if AgreementType.objects.filter(agreement_type=agreementtypeformvalue).exists():
            messages.info(request, 'Agreement Type already exists')
            return redirect('Agreementtype_form')
        else :
            newagreementtype = AgreementType.objects.create(agreement_type=agreementtypeformvalue)
            newagreementtype.save()
            return redirect('Master_details')

    return render(request, 'master/AgreementType.html')


def Applicanttype_form(request):
    if request.method == 'POST':
        applicanttypeformvalue = request.POST['ApplicantType'].strip()
        if ApplicantType.objects.filter(applicant_type=applicanttypeformvalue).exists():
            messages.info(request, 'Applicant Type already exists')
            return redirect('Applicanttype_form')
        else :
            newapplicanttype = ApplicantType.objects.create(applicant_type=applicanttypeformvalue)
            newapplicanttype.save()
            return redirect('Master_details')
    return render(request, 'master/ApplicantType.html')

def AYyear_form(request):
    if request.method == 'POST':
        ayyearformvalue = request.POST['AyYear'].strip()
        if AYYear.objects.filter(ay_year=ayyearformvalue).exists():
            messages.info(request, 'Ay Year already exists')
            return redirect('AYyear_form')
        else :
            newayyear = AYYear.objects.create(ay_year=ayyearformvalue)
            newayyear.save()
            return redirect('Master_details')
    return render(request, 'master/AyYear.html')

def NatureOfBusiness_form(request):
    if request.method == 'POST':
        natureofbusinessformvalue = request.POST['NatureBusiness'].strip()
        if NatureOfBusiness.objects.filter(nature_business=natureofbusinessformvalue).exists():
            messages.info(request, 'Nature of Business already exists')
            return redirect('NatureOfBusiness_form')
        else :
            newnatureofbusiness = NatureOfBusiness.objects.create(nature_business=natureofbusinessformvalue)
            newnatureofbusiness.save()
            return redirect('Master_details')
    return render(request, 'master/NatureOfBusiness.html')

def PropertyIn_form(request):
    if request.method == 'POST':
        propertyinformvalue = request.POST['PropertyIn'].strip()
        if PropertyIn.objects.filter(property_in=propertyinformvalue).exists():
            messages.info(request, 'PropertyIn Business already exists')
            return redirect('PropertyIn_form')
        else :
            newpropertyin = PropertyIn.objects.create(property_in=propertyinformvalue)
            newpropertyin.save()
            return redirect('Master_details')
    return render(request, 'master/PropertyIn.html')

def RejectionType_form(request):
    if request.method == 'POST':
        rejectiontypeformvvalue = request.POST['Type'].strip()
        rejectiontypereasonformvvalue = request.POST['Reason'].strip()
        if RejectionType.objects.filter(rejection_type=rejectiontypeformvvalue, rejection_reason=rejectiontypereasonformvvalue).exists():
            messages.info(request, 'Rejection type already exists')
            return redirect('RejectionType_form')
        else :
            newrejectiontype = RejectionType.objects.create(rejection_type=rejectiontypeformvvalue, rejection_reason=rejectiontypereasonformvvalue)
            newrejectiontype.save()
            return redirect('Master_details')

    return render(request, 'master/RejectionType.html')

def StageOfConstruction_form(request):
    if request.method == 'POST':
        stageformvalue = request.POST['Stage'].strip()
        if StageOfConstruction.objects.filter(stage=stageformvalue).exists():
            messages.info(request, 'Stage Of Construction already exists')
            return redirect('StageOfConstruction_form')
        else :
            newstage = StageOfConstruction.objects.create(stage=stageformvalue)
            newstage.save()
            return redirect('Master_details')
    return render(request, 'master/StageOfConstruction.html')

def Status_form(request):
    if request.method == 'POST':
        statusformvalue = request.POST['Status'].strip()
        if Status.objects.filter(status=statusformvalue).exists():
            messages.info(request, 'Status already exists')
            return redirect('Status_form')
        else :
            newstatus = Status.objects.create(status=statusformvalue)
            newstatus.save()
            return redirect('Master_details')
    return render(request, 'master/Status.html')

def CompanyType_form(request):
    if request.method == 'POST':
        companytypeformvalue = request.POST['CompanyType'].strip()
        if CompanyType.objects.filter(company_type=companytypeformvalue).exists():
            messages.info(request, 'Company Type already exists')
            return redirect('CompanyType_form')
        else :
            newcompanytype = CompanyType.objects.create(company_type=companytypeformvalue)
            newcompanytype.save()
            return redirect('Master_details')
    return render(request, 'master/CompanyType.html')

def CustomerType_form(request):
    if request.method == 'POST':
        customertypeformvalue = request.POST['CustomerType'].strip()
        if CustomerType.objects.filter(cust_type=customertypeformvalue).exists():
            messages.info(request, 'Customer Type already exists')
            return redirect('CustomerType_form')
        else :
            newcustomertype = CustomerType.objects.create(cust_type=customertypeformvalue)
            newcustomertype.save()
            return redirect('Master_details')
    return render(request, 'master/CustomerType.html')

def DesignationType_form(request):
    if request.method == 'POST':
        designationtypeformvalue = request.POST['DesignationType'].strip()
        if DesignationType.objects.filter(desg_type=designationtypeformvalue).exists():
            messages.info(request, 'Designation Type already exists')
            return redirect('DesignationType_form')
        else :
            newdesignationtype = DesignationType.objects.create(desg_type=designationtypeformvalue)
            newdesignationtype.save()
            return redirect('Master_details')
    return render(request, 'master/DesignationType.html')

def Product_form(request):
    if request.method == 'POST':
        productformvalue = request.POST['Product'].strip()
        if Product.objects.filter(product=productformvalue).exists():
            messages.info(request, 'Product already exists')
            return redirect('Product_form')
        else :
            newProduct = Product.objects.create(product=productformvalue)
            newProduct.save()
            return redirect('Master_details')
    return render(request, 'master/Product.html')

def Profession_form(request):
    if request.method == 'POST':
        professionformvalue = request.POST['Profession'].strip()
        if Profession.objects.filter(profession=professionformvalue).exists():
            messages.info(request, 'Profession already exists')
            return redirect('Profession_form')
        else :
            newprofession = Profession.objects.create(profession=professionformvalue)
            newprofession.save()
            return redirect('Master_details')
    return render(request, 'master/Profession.html')

def Qualification_form(request):
    if request.method == 'POST':
        qualificationformvalue = request.POST['Qualification'].strip()
        if Qualification.objects.filter(qualification=qualificationformvalue).exists():
            messages.info(request, 'qualification already exists')
            return redirect('qualification_form')
        else :
            newqualification = Qualification.objects.create(qualification=qualificationformvalue)
            newqualification.save()
            return redirect('Master_details')
    return render(request, 'master/Qualification_Details.html')

def Role_form(request):
    if request.method == 'POST':
        roleformvalue = request.POST['Role'].strip()
        if Role.objects.filter(role=roleformvalue).exists():
            messages.info(request, 'Role already exists')
            return redirect('Role_form')
        else :
            newrole = Role.objects.create(role=roleformvalue)
            newrole.save()
            return redirect('Master_details')
    return render(request, 'master/Role.html')

def BankName_form(request):
    if request.method == 'POST':
        banknameformvalue = request.POST['bankName'].strip()
        if BankName.objects.filter(bank_name=banknameformvalue).exists():
            messages.info(request, 'Bank Name already exists')
            return redirect('BankName_form')
        else :
            newbankname = BankName.objects.create(bank_name=banknameformvalue)
            newbankname.save()
            return redirect('Master_details')
    return render(request, 'master/bank_name.html')

def Degree_form(request):
    if request.method == 'POST':
        degreeformvalue = request.POST['degree'].strip()
        if Degree.objects.filter(degree=degreeformvalue).exists():
            messages.info(request, 'Degree already exists')
            return redirect('Degree_form')
        else :
            newdegree = Degree.objects.create(degree=degreeformvalue)
            newdegree.save()
            return redirect('Master_details')
    return render(request, 'master/degree.html')

def LeadSource_form(request):
    if request.method == 'POST':
        leadsourceformvalue = request.POST['leadSource'].strip()
        if LeadSource.objects.filter(lead_source=leadsourceformvalue).exists():
            messages.info(request, 'Degree already exists')
            return redirect('LeadSource_form')
        else :
            newleadsource = LeadSource.objects.create(lead_source=leadsourceformvalue)
            newleadsource.save()
            return redirect('Master_details')
    return render(request, 'master/lead_source.html')

def Nationality_form(request):
    if request.method == 'POST':
        nationalityformvalue = request.POST['nation'].strip()
        if Nationality.objects.filter(nationality=nationalityformvalue).exists():
            messages.info(request, 'Degree already exists')
            return redirect('Nationality_form')
        else :
            newnationality = Nationality.objects.create(nationality=nationalityformvalue)
            newnationality.save()
            return redirect('Master_details')
    return render(request, 'master/nationality.html')

def ResidenceType_form(request):
    if request.method == 'POST':
        residencetypeformvalue = request.POST['resType'].strip()
        if ResidenceType.objects.filter(residence_type=residencetypeformvalue).exists():
            messages.info(request, 'Residence Type already exists')
            return redirect('ResidenceType_form')
        else :
            newresidencetype = ResidenceType.objects.create(residence_type=residencetypeformvalue)
            newresidencetype.save()
            return redirect('Master_details')
    return render(request, 'master/residence_type.html')

def SalaryType_form(request):
    if request.method == 'POST':
        salarytypeformvalue = request.POST['salaryType'].strip()
        if SalaryType.objects.filter(salary_type=salarytypeformvalue).exists():
            messages.info(request, 'Salary Type already exists')
            return redirect('SalaryType_form')
        else :
            newsalarytype = SalaryType.objects.create(salary_type=salarytypeformvalue)
            newsalarytype.save()
            return redirect('Master_details')
    return render(request, 'master/salary_type.html')

def State_form(request):
    if request.method == 'POST':
        stateformvalue = request.POST['state'].strip()
        if State.objects.filter(state=stateformvalue).exists():
            messages.info(request, 'State already exists')
            return redirect('State_form')
        else :
            newstate = State.objects.create(state=stateformvalue)
            newstate.save()
            return redirect('Master_details')
    return render(request, 'master/state.html')

def SubProduct_form(request):
    if request.method == 'POST':
        product = Product.objects.get(pk=int(request.POST['product']))
        subproductformvalue = request.POST['SubProduct'].strip()
        if SubProduct.objects.filter(sub_product=subproductformvalue, product=product).exists():
            messages.info(request, 'Sub Product already exists')
            return redirect('SubProduct_form')
        else :
            newsubproduct = SubProduct.objects.create(sub_product=subproductformvalue, product=product)
            newsubproduct.save()
            return redirect('Master_details')

    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'master/SubProduct.html', context=context)

def City_form(request):
    if request.method == 'POST':
        state = State.objects.get(pk=int(request.POST['state']))
        cityformvalue = request.POST['city'].strip()
        if City.objects.filter(city_name=cityformvalue, state=state).exists():
            messages.info(request, 'city already exists')
            return redirect('City_form')
        else :
            newcity = City.objects.create(city_name=cityformvalue, state=state)
            newcity.save()
            return redirect('Master_details')

    states = State.objects.all()
    context = {
        'states':states
    }
    return render(request, 'master/city.html', context=context)


def Masterdetails(request):

    print(SubProduct.objects.all()[0].product.product)

    context = {
        'qualifications': Qualification.objects.all(),
        'professions': Profession.objects.all(),
        'roles': Role.objects.all(),
        'products': Product.objects.all(),
        'subproducts': SubProduct.objects.all(),
        'customertypes': CustomerType.objects.all(),
        'designationtypes': DesignationType.objects.all(),
        'companytypes': CompanyType.objects.all(),
        'salarytypes': SalaryType.objects.all(),
        'residencetypes': ResidenceType.objects.all(),
        'banknames': BankName.objects.all(),
        'leadsources': LeadSource.objects.all(),
        'degrees': Degree.objects.all(),
        'nationalitys': Nationality.objects.all(),
        'states': State.objects.all(),
        'citys': City.objects.all(),
        'applicanttypes': ApplicantType.objects.all(),
        'propertyins': PropertyIn.objects.all(),
        'statues': Status.objects.all(),
        'natureofbusinesss': NatureOfBusiness.objects.all(),
        'ayyears': AYYear.objects.all(),
        'agreementtypes': AgreementType.objects.all(),
        'stageOfconstructions': StageOfConstruction.objects.all(),
        'rejectiontypes': RejectionType.objects.all(),

    }
    return render(request, 'master/master_details.html', context=context)

def editqualification(request, id):
    if request.method == 'POST':
        qualification = Qualification.objects.filter(id=id)
        newqualification = request.POST['Qualification']
        qualification.update(qualification=newqualification)
        return redirect('Master_details')
    print(Qualification.objects.filter(id=id)[0])
    context = {
        'qualification': Qualification.objects.filter(id=id)[0]
    }
    return render(request, 'master/qualification_edit.html', context=context)

def editprofession(request, id):
    if request.method == 'POST':
        profession = Profession.objects.filter(id=id)
        newprofession = request.POST['Profession']
        profession.update(profession=newprofession)
        return redirect('Master_details')
    print(Profession.objects.filter(id=id)[0])
    context = {
        'profession': Profession.objects.filter(id=id)[0]
    }
    return render(request, 'master/profession_edit.html', context=context)

def editrole(request, id):
    if request.method == 'POST':
        role = Role.objects.filter(id=id)
        newrole = request.POST['Role']
        role.update(role=newrole)
        return redirect('Master_details')
    print(Role.objects.filter(id=id)[0])
    context = {
        'role': Role.objects.filter(id=id)[0]
    }
    return render(request, 'master/role_edit.html', context=context)

def editproduct(request, id):
    if request.method == 'POST':
        product =Product.objects.filter(id=id)
        newproduct = request.POST['Product']
        product.update(product=newproduct)
        return redirect('Master_details')
    print(Product.objects.filter(id=id)[0])
    context = {
        'product': Product.objects.filter(id=id)[0]
    }
    return render(request, 'master/product_edit.html', context=context)

def editsubproduct(request, id):
    if request.method == 'POST':
        sub_product = SubProduct.objects.filter(id=id)
        newsubproduct = request.POST['SubProduct']
        sub_product.update(sub_product=newsubproduct)
        return redirect('Master_details')
    print(SubProduct.objects.filter(id=id)[0])
    context = {
        'product': SubProduct.objects.filter(id=id)[0]
    }
    return render(request, 'master/subproduct_edit.html', context=context)

def editcustomertype(request, id):
    if request.method == 'POST':
        cust_type = CustomerType.objects.filter(id=id)
        newcusttype = request.POST['CustomerType']
        cust_type.update(cust_type=newcusttype)
        return redirect('Master_details')
    print(CustomerType.objects.filter(id=id)[0])
    context = {
        'cust_type': CustomerType.objects.filter(id=id)[0]
    }
    return render(request, 'master/customertype_edit.html', context=context)

def editdesignationtype(request, id):
    if request.method == 'POST':
        desg_type = DesignationType.objects.filter(id=id)
        newdesgtype = request.POST['DesignationType']
        desg_type.update(desg_type=newdesgtype)
        return redirect('Master_details')
    print(DesignationType.objects.filter(id=id)[0])
    context = {
        'desg_type': DesignationType.objects.filter(id=id)[0]
    }
    return render(request, 'master/designationtype_edit.html', context=context)

def editcompanytype(request, id):
    if request.method == 'POST':
        company_type = CompanyType.objects.filter(id=id)
        newcomptype = request.POST['CompanyType']
        company_type.update(company_type=newcomptype)
        return redirect('Master_details')
    print(CompanyType.objects.filter(id=id)[0])
    context = {
        'company_type': CompanyType.objects.filter(id=id)[0]
    }
    return render(request, 'master/companytype_edit.html', context=context)

def editsalarytype(request, id):
    if request.method == 'POST':
        salary_type = SalaryType.objects.filter(id=id)
        newsaltype = request.POST['salaryType']
        salary_type.update(salary_type=newsaltype)
        return redirect('Master_details')
    print(SalaryType.objects.filter(id=id)[0])
    context = {
        'salary_type': SalaryType.objects.filter(id=id)[0]
    }
    return render(request, 'master/salarytype_edit.html', context=context)

def editresidencetype(request, id):
    if request.method == 'POST':
        residence_type = ResidenceType.objects.filter(id=id)
        newrestype = request.POST['resType']
        residence_type.update(residence_type=newrestype)
        return redirect('Master_details')
    print(ResidenceType.objects.filter(id=id)[0])
    context = {
        'residence_type': ResidenceType.objects.filter(id=id)[0]
    }
    return render(request, 'master/residencetype_edit.html', context=context)

def editbankname(request, id):
    if request.method == 'POST':
        bank_name = BankName.objects.filter(id=id)
        newbankname = request.POST['bankName']
        bank_name.update(bank_name=newbankname)
        return redirect('Master_details')
    print(BankName.objects.filter(id=id)[0])
    context = {
        'bank_name': BankName.objects.filter(id=id)[0]
    }
    return render(request, 'master/editbankname.html', context=context)

def editleadsource(request, id):
    if request.method == 'POST':
        lead_source = LeadSource.objects.filter(id=id)
        newleadsource = request.POST['leadSource']
        lead_source.update(lead_source=newleadsource)
        return redirect('Master_details')
    print(LeadSource.objects.filter(id=id)[0])
    context = {
        'lead_source': LeadSource.objects.filter(id=id)[0]
    }
    return render(request, 'master/leadsourceedit.html', context=context)

def editdegree(request, id):
    if request.method == 'POST':
        degree = Degree.objects.filter(id=id)
        newdegree = request.POST['degree']
        degree.update(degree=newdegree)
        return redirect('Master_details')
    print(Degree.objects.filter(id=id)[0])
    context = {
        'degree': Degree.objects.filter(id=id)[0]
    }
    return render(request, 'master/degree_edit.html', context=context)

def editnationality(request, id):
    if request.method == 'POST':
        nationality = Nationality.objects.filter(id=id)
        newnation = request.POST['nation']
        nationality.update(nationality=newnation)
        return redirect('Master_details')
    print(Nationality.objects.filter(id=id)[0])
    context = {
        'nationality': Nationality.objects.filter(id=id)[0]
    }
    return render(request, 'master/nationality_edit.html', context=context)

def editstate(request, id):
    if request.method == 'POST':
        state = State.objects.filter(id=id)
        newstate = request.POST['state']
        state.update(state=newstate)
        return redirect('Master_details')
    print(State.objects.filter(id=id)[0])
    context = {
        'state': State.objects.filter(id=id)[0]
    }
    return render(request, 'master/state_edit.html', context=context)

def editcity(request, id):
    if request.method == 'POST':
        city_name = City.objects.filter(id=id)
        newcity = request.POST['city']
        city_name.update(city_name=newcity)
        return redirect('Master_details')
    print(City.objects.filter(id=id)[0])
    context = {
        'city_name': City.objects.filter(id=id)[0]
    }
    return render(request, 'master/city_edit.html', context=context)

def editapplicanttype(request, id):
    if request.method == 'POST':
        applicant_type = ApplicantType.objects.filter(id=id)
        newapplicant = request.POST['ApplicantType']
        applicant_type.update(applicant_type=newapplicant)
        return redirect('Master_details')
    print(ApplicantType.objects.filter(id=id)[0])
    context = {
        'applicant_type': ApplicantType.objects.filter(id=id)[0]
    }
    return render(request, 'master/applicant_edit.html', context=context)

def editpropertyln(request, id):
    if request.method == 'POST':
        property_in = PropertyIn.objects.filter(id=id)
        newapropertyln = request.POST['PropertyIn']
        property_in.update(property_in=newapropertyln)
        return redirect('Master_details')
    print(PropertyIn.objects.filter(id=id)[0])
    context = {
        'property_in': PropertyIn.objects.filter(id=id)[0]
    }
    return render(request, 'master/propertyin_edit.html', context=context)

def editstatus(request, id):
    if request.method == 'POST':
        status = Status.objects.filter(id=id)
        newstatus = request.POST['Status']
        status.update(status=newstatus)
        return redirect('Master_details')
    print(Status.objects.filter(id=id)[0])
    context = {
        'status': Status.objects.filter(id=id)[0]
    }
    return render(request, 'master/status_edit.html', context=context)

def editnatureofbusiness(request, id):
    if request.method == 'POST':
        nature_business = NatureOfBusiness.objects.filter(id=id)
        newbusiness = request.POST['NatureBusiness']
        nature_business.update(nature_business=newbusiness)
        return redirect('Master_details')
    print(NatureOfBusiness.objects.filter(id=id)[0])
    context = {
        'nature_business': NatureOfBusiness.objects.filter(id=id)[0]
    }
    return render(request, 'master/natureofbusiness_edit.html', context=context)

def editayyear(request, id):
    if request.method == 'POST':
        ay_year = AYYear.objects.filter(id=id)
        newayyear = request.POST['AyYear']
        ay_year.update(ay_year=newayyear)
        return redirect('Master_details')
    print(AYYear.objects.filter(id=id)[0])
    context = {
        'ay_year': AYYear.objects.filter(id=id)[0]
    }
    return render(request, 'master/ayyear_edit.html', context=context)

def editagreementtype(request, id):
    if request.method == 'POST':
        agreement_type = AgreementType.objects.filter(id=id)
        newagreementtype = request.POST['AgreementType']
        agreement_type.update(agreement_type=newagreementtype)
        return redirect('Master_details')
    print(AgreementType.objects.filter(id=id)[0])
    context = {
        'agreement_type': AgreementType.objects.filter(id=id)[0]
    }
    return render(request, 'master/agreement_edit.html', context=context)

def editstageofconstruction(request, id):
    if request.method == 'POST':
        stage = StageOfConstruction.objects.filter(id=id)
        newstage = request.POST['Stage']
        stage.update(stage=newstage)
        return redirect('Master_details')
    print(StageOfConstruction.objects.filter(id=id)[0])
    context = {
        'stage': StageOfConstruction.objects.filter(id=id)[0]
    }
    return render(request, 'master/stageofconstruction_edit.html', context=context)

def editrejectiontype(request, id):
    if request.method == 'POST':
        rejection_type = RejectionType.objects.filter(id=id)
        newrejection = request.POST['Reason']
        rejection_type.update(rejection_type=newrejection)
        return redirect('Master_details')
    print(RejectionType.objects.filter(id=id)[0])
    context = {
        'rejection_type': RejectionType.objects.filter(id=id)[0]
    }
    return render(request, 'master/rejection_edit.html', context=context)
