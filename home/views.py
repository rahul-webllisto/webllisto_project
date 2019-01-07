from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
from .forms import *
from .functions import *
# Create your views here.

def home_page(request):
	obj = Teacher.objects.all()
	contact_obj = Contact.objects.all()
	resume_obj = CollectResume.objects.all()

	# contact form
	if request.method == 'POST':
		form_data = ContactForm(request.POST)

		if form_data.is_valid():
			user_name = form_data.cleaned_data['user_name']
			user_phone = form_data.cleaned_data['user_phone']
			user_email = form_data.cleaned_data['user_email']
			user_details = form_data.cleaned_data['user_details']

			d = Contact(user_name=user_name, user_phone=user_phone, user_email=user_email, user_details=user_details)
			d.save()

			return HttpResponse('<div class="alert alert-success"> Your Form Submit successfully </div>')
	
	contact_form = ContactForm()

	# resume form
	if request.method == 'POST':
		form_data = CollectResumeForm(request.POST, request.FILES)

		if form_data.is_valid():
			form_data.save()

			return HttpResponse('Your form submit successfully.')
	

	resume_form = CollectResumeForm()

	#job apply form
	applyform = JobApplyForm()

	if request.method == 'POST':
		applyform = JobApplyForm(request.POST, request.FILES)

		if applyform.is_valid():
			applyform.save()
			return HttpResponse('Your form submit successfully.')


	return render(request,'home.html',{'contact': contact_form, 'resume': resume_form, 'apply': applyform})

