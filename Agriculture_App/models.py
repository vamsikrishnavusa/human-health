from django.db import models

# Create your models here.

class AdminDetails(models.Model):
	username = models.CharField(max_length=100,default=None)
	password = models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'AdminDetails'


class UserDetails(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    Address = models.CharField(max_length=100,default=None,null=True)
    Area=models.CharField(max_length=100,default=None,null=True)
    phone = models.CharField(max_length=15)  
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'UserDetails'


class Doctor(models.Model):
	registeratio_number = models.TextField(max_length=100, default=None)
	College= models.TextField(max_length=100,default=None)
	Year= models.TextField(max_length=100,default=None)
	Name 		= models.TextField(max_length=100,default=None)
	Picture 	= models.ImageField(upload_to="images/",null=True)
	username 	= models.TextField(max_length=100,default=None)
	password 	= models.TextField(max_length=100,default=None)
	Age 		= models.TextField(max_length=100,default=None)
	Gender 		= models.TextField(max_length=100,default=None)
	Phone 		= models.TextField(max_length=100,default=None)
	Area		= models.TextField(max_length=100,default=None)
	State		= models.TextField(max_length=100,default=None)
	City		= models.TextField(max_length=100,default=None)
	Address 	= models.TextField(max_length=100,default=None)
	Start_time  = models.DateTimeField(max_length=100,default=None,null = True)
	End_Time 	= models.DateTimeField(max_length=100,default=None,null = True)
	Speciality 	= models.TextField(max_length=100,default=None)
	Type_of_medicine = models.TextField(max_length=100,default=None)
	Permission 	= models.TextField(max_length=100,default=None,null=True)
	Disease_treated = models.TextField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'Doctor'


class Appointment(models.Model):
	Doctor= models.TextField(max_length=155500,default=None,null=True)
	Patient= models.TextField(max_length=155500,default=None,null=True)
	Booking_Date_Time= models.DateTimeField(max_length=155500,default=None,null=True)
	Start_time  = models.TimeField(max_length=100,default=None)
	End_Time 	= models.TimeField(max_length=100,default=None)
	#Duration= models.TextField(max_length=155500,default=None,null=True)
	Reason= models.TextField(max_length=155500,default=None,null=True)
	Appointment_Status= models.TextField(max_length=155500,default=None,null=True)
	#Created_Date= models.DateTimeField(max_length=155500,default=None,null=True)
	Updated_Date_Time = models.DateTimeField(max_length=155500,default=None,null=True)
	Prescription= models.TextField(max_length=155500,default=None,null=True)
	Diagnosis= models.TextField(max_length=155500,default=None,null=True)
	Follow_Up_Instructions= models.TextField(max_length=155500,default=None,null=True)
	Speciality_Type= models.TextField(max_length=155500,default=None,null=True)
	Lab_Tests = models.TextField(max_length=155500,default=None,null=True)
	Imaging_Tests = models.TextField(max_length=155500,default=None,null=True)
	Billing_and_Payment= models.TextField(max_length=155500,default=None,null=True)
	Medical_History = models.TextField(max_length=155500,default=None,null=True)
	Treatment_Status = models.TextField(max_length=155500,default="Pending",null=True)
	Fee_status = models.TextField(max_length=155500,default="Pending",null=True)
	#Meeting_status = models.TextField(max_length=155500,default="Pending",null=True)
	#Room_name = models.TextField(max_length=155500,default=None,null=True)

	

	class Meta:
		db_table = "Appointment"



class User_Feedback(models.Model):
	user = models.CharField(max_length=100,default=None,null=True)
	feedback = models.CharField(max_length=500,default=None,null=True)
	response = models.CharField(max_length=500,default=None,null=True)
	class Meta:
		db_table = "User_Feedback"


class Doctor_Feedback(models.Model):
	doctor = models.CharField(max_length=100,default=None,null=True)
	feedback = models.CharField(max_length=500,default=None,null=True)
	response = models.CharField(max_length=500,default=None,null=True)
	class Meta:
		db_table = "Doctor_Feedback"
