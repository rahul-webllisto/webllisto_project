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

class JobApplyForm(ModelForm):
	class Meta:
		model = JobApply
		fields = '__all__'
