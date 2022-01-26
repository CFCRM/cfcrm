from typing import Text, Type
from django.forms import DateField, widgets
from django import forms
from django.forms.models import ModelChoiceField, ModelForm
from django.forms.widgets import EmailInput, NumberInput, TextInput
from .models import *
from django.db.models import Q


class HlBasicDetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HlBasicDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = HlBasicDetails
        exclude = ('basic_details_id',)


class HlObligationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HlObligationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = HlObligation
        exclude = ('basic_details_id',)


class HlOtherDetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HlOtherDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = HlOtherDetails
        exclude = ('basic_details_id',)


class HlPropertyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HlPropertyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = HlProperty
        exclude = ('basic_details_id',)


class HlLoan_To_Value_Type_1Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HlLoan_To_Value_Type_1Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = HlLoan_To_Value_Type_1
        exclude = ('basic_details_id',)


class HlLoan_To_Value_Type_2Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HlLoan_To_Value_Type_2Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = HlLoan_To_Value_Type_2
        exclude = ('basic_details_id',)
    

class HlIncomeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HlIncomeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = HlIncome
        exclude = ('basic_details_id',)
