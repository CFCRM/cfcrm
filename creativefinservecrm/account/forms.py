from typing import Text, Type
from django.forms import DateField, widgets
from django import forms
from django.forms.models import ModelChoiceField, ModelForm
from django.forms.widgets import EmailInput, NumberInput, TextInput
from .models import *
from django.db.models import Q

class LeadsForm(ModelForm):
    class Meta:
        model = Leads
        exclude = ('added_by',)
    def __init__(self, *args, **kwargs):
        super(LeadsForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'autofocus':''
            })
        self.fields['sub_product'].queryset = SubProduct.objects.none() 
        self.fields['city'].queryset = SubProduct.objects.none() 

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state = state_id)
            except(ValueError,TypeError):
                pass
        
        if 'product' in self.data:
            try:
                product_id = int(self.data.get('product'))
                self.fields['sub_product'].queryset = SubProduct.objects.filter(product = product_id)
            except(ValueError,TypeError):
                pass
        


class TempForm(forms.Form):
    applicant_type = forms.ModelChoiceField(queryset = ApplicantType.objects.filter(~Q(applicant_type = 'Applicant')))
    applicant_type.widget.attrs.update({'class':'form-control','id':'select_applicant_type'})

class AdditionalDetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdditionalDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['applicant_type'].widget.attrs.update({'readonly': 'true'})
        self.fields['is_diff'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = AdditionalDetails
        exclude = ('lead_id',)

class PropertyDetailsType1Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyDetailsType1Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = PropType1
        exclude = ('lead_id',)
        widgets = {
            'possession_date': widgets.DateInput(attrs={'type': 'date'})
        }


class PropertyType2Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyType2Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    def clean_data(self):
        cleaned_data = super(PropertyType2Form, self).clean()
        cc_rec = cleaned_data.get('cc_rec')
        cost_sheet = cleaned_data.get('cost_sheet')
        car_parking = cleaned_data.get('car_parking')
        if cc_rec == True:
            if not cleaned_data.get('cc_rec_upto'):
                raise forms.ValidationError("Please enter cc_rec")
        if cost_sheet == True:
            if not cleaned_data.get('cost_sheet_amt'):
                raise forms.ValidationError("Please enter cost_sheet amount")
        if car_parking == True:
            if not cleaned_data.get('car_parking_amt'):
                raise forms.ValidationError("Please enter car parking amt")
    class Meta:
        model = PropType2
        exclude = ('lead_id',)
        widgets = {
            'possession_date': widgets.DateInput(attrs={'type': 'date'})
        }
 


class PropType3Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropType3Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = PropType3
        exclude = ('lead_id',)


class PropType4Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropType4Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = PropType4
        exclude = ('lead_id',)

class SalIncomeDetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SalIncomeDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = SalIncomeDetails
        exclude = ('inc_det_id', 'addi_details_id',)


class SalOtherIncomesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SalOtherIncomesForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = SalOtherIncomes
        exclude = ('other_inc_det_id', 'addi_details_id_other_inc',)


# class ContactPersonForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ContactPersonForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form-control'})

#     class Meta:
#         model = ContactPerson
#         exclude = ('con_id', 'add_det_id',)


class SalPersonalDetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SalPersonalDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = SalPersonalDetails
        exclude = ('additional_details_id', 'per_det_id',)
        widgets = {
            'dob': widgets.DateInput(attrs={'type': 'date'})
        }
    
