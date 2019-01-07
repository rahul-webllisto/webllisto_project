from django.db import models

# Create your models here.
class Teacher(models.Model):
	email = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)


class Student(models.Model):
	student_name = models.CharField(max_length=100)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	student_email = models.CharField(max_length=255, blank=True)

class Contact(models.Model):
	user_name = models.CharField(max_length=100)
	user_phone = models.CharField(max_length=20)
	user_email = models.EmailField(max_length=50)
	user_details = models.CharField(max_length=255)

class CollectResume(models.Model):
	user_name = models.CharField(max_length=100)
	user_phone = models.SmallIntegerField()
	user_email = models.EmailField(max_length=50)
	user_exp = models.SmallIntegerField()
	user_current_ctc = models.SmallIntegerField()
	user_resume = models.FileField(max_length=50, upload_to='uploads/%Y/%m/%d/')
	user_msg = models.TextField(max_length=225)
	current_date = models.DateTimeField(auto_now=True)

class JobApply(models.Model):
	#Choices
	Gender = (('male', 'Male'),('female', 'Female'))
	Qual = (('B.E', 'B.E'),('M.Sc', 'M.Sc'))
	YoQual = ((2015,2015), (2016,2016), (2017,2017))
	Marital = (('married','married'), ('un-married','un-married'))
	Exp = (('1 year', '1 year'), ('2 year', '2 year'), ('3 year', '3 year'))
	TExp = (('1 year', '1 year'), ('2 year', '2 year'), ('3 year', '3 year'))




	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	fathername = models.CharField(max_length=100)
	mothername = models.CharField(max_length=100)
	gender = models.CharField(max_length=6, choices=Gender)
	high_qual = models.CharField(max_length=6, choices=Qual)
	year_of_qual = models.CharField(max_length=6, choices=YoQual)
	marital = models.CharField(max_length=6, choices=Marital)
	act_exp = models.CharField(max_length=6, choices=Exp)
	total_exp = models.CharField(max_length=6, choices=TExp)
	emailid = models.EmailField(max_length=50)
	contact_no = models.SmallIntegerField()
	alt_contact_no = models.SmallIntegerField()

	# past and present

	employer_name = models.CharField(max_length=50)
	employer_location = models.CharField(max_length=150)
	employer_location = models.CharField(max_length=150)
	startdate = models.DateField()
	endtdate = models.DateField()
	skills = models.CharField(max_length=255)
	state = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	area = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	pincode = models.SmallIntegerField()
	resume = models.FileField(max_length=50, upload_to='uploads/%Y/%m/%d/')





