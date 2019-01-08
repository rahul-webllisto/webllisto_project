from django import forms
from django.forms import ModelForm
from .models import *

class ContactForm(forms.Form):
	user_name = forms.CharField(max_length=100)
	user_phone = forms.CharField(max_length=20)
	user_email = forms.EmailField(max_length=50)
	user_details = forms.CharField(max_length=255, widget=forms.Textarea)

	user_name.widget.attrs.update({'class': 'form-control','placeholder': 'Name'})
	user_phone.widget.attrs.update({'class': 'form-control','placeholder': 'Phone'})
	user_email.widget.attrs.update({'class': 'form-control','placeholder': 'Email'})
	user_details.widget.attrs.update({'class': 'form-control','placeholder': 'The Details', 'cols': 0, 'rows': 0})

class CollectResumeForm(ModelForm):
	class Meta:
		model = CollectResume
		fields = '__all__'

class JobApplyForm(forms.ModelForm):

	Gender = (('Gender','Gender'),('Male', 'Male'),('Female', 'Female'))
	Qual = (('qual','Qualification'),('B.E', 'B.E'),('M.Sc', 'M.Sc'))
	YoQual = (('yoq','Year Of Qualification'),('2015','2015'), ('2016','2016'), ('2017','2017'))
	Marital = (('Marital','Marital Status'),('married','Married'), ('un-married','Un-married'))
	Exp = (('Exp','Experience'),('1 year', '1 year'), ('2 year', '2 year'), ('3 year', '3 year'))
	TExp = (('TExp','Total Experience'),('1 year', '1 year'), ('2 year', '2 year'), ('3 year', '3 year'))

	gender = forms.ChoiceField(choices=Gender, label='Gender')
	high_qual = forms.ChoiceField(choices=Qual, label='Qualification')
	year_of_qual = forms.ChoiceField(choices=YoQual,label='Year Of Qualification')
	marital = forms.ChoiceField(choices=Marital, label='Marital Status')
	act_exp = forms.ChoiceField(choices=Exp, label='Experience')
	total_exp = forms.ChoiceField(choices=TExp, label='Total Experience')

	class Meta:
		model = JobApply
		fields = '__all__'
		