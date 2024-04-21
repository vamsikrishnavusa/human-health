from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db import connection
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from django.db.models import Q
from django.utils import timezone
from datetime import date
from django.db.models import Sum
import time
import datetime

# Create your views here.	


def Home(request):
	return render(request,"Home.html",{})

def Admin_Login(request):
	if request.method == "POST":
		A_username = request.POST['aname']
		A_password = request.POST['apass']
		if AdminDetails.objects.filter(username = A_username,password = A_password).exists():
			ad = AdminDetails.objects.get(username=A_username, password=A_password)
			print('d')
			messages.info(request,'Admin login is Sucessfull')
			request.session['type_id'] = 'Admin'
			request.session['UserType'] = 'Admin'
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
			return render(request, "Admin_Login.html", {})
	else:
		return render(request, "Admin_Login.html", {})


def User_Login(request):
    if request.method == "POST":
        A_username = request.POST['aname']
        A_password = request.POST['apass']
        if UserDetails.objects.filter(username=A_username, password=A_password).exists():
            users = UserDetails.objects.all().filter(username=A_username, password=A_password)
            messages.info(request,A_username+ ' logged in')
            request.session['UserId'] = users[0].id
            request.session['type_id'] = 'User'
            request.session['UserType'] = A_username
            request.session['login'] = "Yes"
            request.session['Area'] = users[0].Area
            return redirect("/")
        else:
            messages.error(request, 'Not Registered')
            return redirect("/User_Registration/")
    else:
        return render(request,'User_Login.html',{})



def Doctor_Login(request):
	if request.method == "POST":
		C_name = request.POST['aname']
		C_password = request.POST['apass']
		if Doctor.objects.filter(username=C_name, password=C_password,Permission="Accepted").exists():
			users = Doctor.objects.all().filter(username=C_name, password=C_password)
			messages.info(request,'Dr. '+C_name+ ' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'Doctor'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			messages.error(request, 'Admin has not Accepted your request')
			return redirect("/Add_Doctor/")
	else:
		return render(request,'Doctor_Login.html',{})
	return render(request,'Doctor_Login.html',{})


def Accept(request,id):
	print("Hello")
	Doctor.objects.filter(id=id).update(Permission="Accepted")
	return redirect('/Manage_Doctor/')



def User_Registration(request):
    if request.method == 'POST':
        # Process the form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password = request.POST.get('password')
        area = request.POST.get('area')

        
        if UserDetails.objects.filter(username=username).exists():
            messages.info(request,"Username already exists")
            return  redirect('/User_Registration/')

        
        employee = UserDetails(
            full_name=full_name,
            email=email,
            phone=phone,
            birth_date=birth_date,
            Address=address,
            gender=gender,
            username=username,
            password=password,
            Area = area
        )
        employee.save()
        messages.info(request,"User Added successfully")
        return redirect('/User_Login/')
    else:
        return render(request,"User_Registration.html")




with open("C:/workspace/Monitoring_human_health_issues_due_to_pesticides_in_agriculture/logistic_regression_model.pkl", 'rb') as file:
	model = pickle.load(file)        

def Prediction(request):
	if request.method == "POST":
		options = request.POST['options']
		print(options)
		symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
		result_list = [1 if element in options else 0 for element in symptoms]
		print(result_list)
		z_reshaped = np.array(result_list).reshape(1, -1)  # Reshape z to have the same number of features as the training data

		logreg_confidence = model.predict_proba(z_reshaped)
		print(logreg_confidence)
		logreg_pred = model.predict(z_reshaped)
		print(logreg_pred[0])
		doctors = Doctor.objects.all().filter(Speciality = logreg_pred[0])
		print(doctors)
		disease = logreg_pred[0]


		max_confidence = max(logreg_confidence[0])
		print("Maximum confidence:", max_confidence)
		#disease_name = "Your Disease"
		google_link = "https://www.google.com/search?q=" + disease
		return render(request,"Prediction.html",{'symptoms':symptoms,'disease':disease,'google_link':google_link})
	else:
		symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
		
		return render(request,"Prediction.html",{'symptoms':symptoms})



def Manage_Doctor(request):
	details = Doctor.objects.all()
	return render(request,"Manage_Doctor.html",{'details':details})


def Add_Doctor(request):
	symptoms = [
    "Fungal infection",
    "Hepatitis C",
    "Hepatitis E",
    "Alcoholic hepatitis",
    "Tuberculosis",
    "Common Cold",
    "Pneumonia",
    "Dimorphic hemmorhoids(piles)",
    "Heart attack",
    "Varicose veins",
    "Hypothyroidism",
    "Hyperthyroidism",
    "Hypoglycemia",
    "Osteoarthristis",
    "Arthritis",
    "(vertigo) Paroymsal Positional Vertigo",
    "Acne",
    "Urinary tract infection",
    "Psoriasis",
    "Hepatitis D",
    "Hepatitis B",
    "Allergy",
    "hepatitis A",
    "GERD",
    "Chronic cholestasis",
    "Drug Reaction",
    "Peptic ulcer diseae",
    "AIDS",
    "Diabetes",
    "Gastroenteritis",
    "Bronchial Asthma",
    "Hypertension",
    "Migraine",
    "Cervical spondylosis",
    "Paralysis (brain hemorrhage)",
    "Jaundice",
    "Malaria",
    "Chicken pox",
    "Dengue",
    "Typhoid",
    "Impetigo"]
	return render(request,"Add_Doctor.html",{'symptoms':symptoms})


def Doctor_Registration(request):
	if request.method == "POST":
		registeratio_number = request.POST['registeratio_number']
		Name = request.POST['Name']
		Picture = request.FILES['Picture']
		Age= request.POST['Age']
		Gender= request.POST['Gender']
		Phone= request.POST['phone']
		State= request.POST['State']
		City= request.POST['City']
		Area= request.POST['Area']
		Address= request.POST['Address']
		Speciality= request.POST['Speciality']
		Type_of_medicine = request.POST['Type_of_medicine']
		Username= request.POST['Username']
		Password= request.POST['Password']
		College= request.POST['College']
		Year= request.POST['Year']
		Disease_treated = request.POST['options']
		obj = Doctor(registeratio_number = registeratio_number,
			Name = Name, 
			Year = Year,
			College = College,
					Picture = Picture, 
					username = Username, 
					password = Password, 
					Age = Age, 
					Gender = Gender, 
					Phone = Phone, 
					Area = Area, 
					State = State, 
					City = City, 
					Address = Address, 
					Speciality = Speciality, 
					Type_of_medicine = Type_of_medicine, 
					Disease_treated = Disease_treated,
					Permission="Rejected")
		obj.save()
		messages.info(request,Name +" Registered")
	return redirect("/Manage_Doctor/")


def Doctor_Edit_Profile(request):
    user_id =request.session['UserId']

    if request.method == "POST":
        Name = request.POST['Name']  # Corrected field name
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        Phone = request.POST['phone']
        Address = request.POST['Address']
        Speciality = request.POST['Speciality']
        Type_of_medicine = request.POST['Type_of_medicine']
        Disease_treated = request.POST['Disease']

        doctor = Doctor.objects.get(id=user_id)

        # Handle image upload
        new_image = request.FILES.get('Picture')
        if new_image:
            doctor.Picture = new_image

        doctor.Name = Name
        doctor.Age = Age
        doctor.Gender = Gender
        doctor.Phone = Phone
        doctor.Address = Address
        doctor.Speciality = Speciality
        doctor.Type_of_medicine = Type_of_medicine
        doctor.Disease_treated = Disease_treated

        doctor.save()

        messages.info(request, "Doctor Details Updated")
        return redirect("/Doctor_Edit_Profile/")
    else:
        user_id = request.session['UserId']
        details = Doctor.objects.filter(id=user_id)
        data = Doctor.objects.get(id=user_id)
        return render(request, "Doctor_Edit_Profile.html", {'details': details,'user_id':user_id,'data':data})


def View_Doctor(request,id):
	details = Doctor.objects.filter(id=id)
	data = Doctor.objects.get(id=id)
	return render(request, "View_Doctor.html", {'details': details,'data':data})


def BookAppointment(request,name):
	print(name)
	# First, filter doctors based on their specialty
	specialty_doctors = Doctor.objects.filter(Disease_treated__contains=name)
	print(specialty_doctors)
	area = request.session['Area']
	print(area)
	#
	# Combine the two querysets and ord Next, filter doctors based on the area
	area_doctors = Doctor.objects.filter(Q(Area=area) & Q(Speciality=name))
	print(area_doctors)
	doctors = specialty_doctors.union(area_doctors).order_by('-Area')
	print(doctors)

	return render(request,"BookAppointment.html",{'doctors':doctors})


def Book_doctor(request,id):
	if Appointment.objects.exists():
		last_id = Appointment.objects.latest('id').id
		print(last_id)
		next_id = last_id + 1
	else:
		next_id = 1  
		print('next id :',next_id)
	print(id)


	data = Doctor.objects.all().filter(id = id)
	d_id = data[0].id
	print(d_id)
	doctor_name = data[0].Name
	doctor_start = data[0].Start_time
	doctor_end = data[0].End_Time
	print(doctor_name)
	print(doctor_start)
	print(doctor_end)
	
	return render(request,"Book_doctor.html",{'next_id':next_id,'d_id':d_id,'doctor_name':doctor_name,'doctor_start':doctor_start,'doctor_end':doctor_end})
	
def BookAppointments(request):
	if request.method == "POST":
		Appointment_id = request.POST['b_id']
		Patient_id = request.session['UserId']
		Doctor_name = request.POST['d_name']
		Doctor_id = request.POST['d_id']
		Booking_Date_Time =  datetime.datetime.now()
		print(Booking_Date_Time)
		Start_time = request.POST['start_time']
		End_Time = request.POST['end_time']
		Reason = request.POST['Reason']
		Appointment_Status = "Pending"
		#Updated_Date_Time = request.POST['options']
		Speciality_Type = Doctor.objects.get(id=Doctor_id)
		Speciality_Type = Speciality_Type.Speciality
		print(Speciality_Type)
		Medical_History = request.POST['Medical_History']

		data = Appointment(id =Appointment_id, Doctor = Doctor_id ,
		Patient = Patient_id ,
		Booking_Date_Time =Booking_Date_Time ,
		Start_time =Start_time ,
		End_Time = End_Time,
		Reason = Reason,
		Appointment_Status = Appointment_Status,
		Speciality_Type =Speciality_Type ,
		Medical_History = Medical_History)
		data.save()
	return redirect('/User_Appointments')


def User_Appointments(request):
	user = request.session['UserId']
	data = Appointment.objects.all().filter(Patient = user)
	return render(request,'User_Appointments.html',{'data':data})


def View_Appointments(request):
	Doctor_id = request.session['UserId']
	data = Appointment.objects.all().filter(Doctor = Doctor_id)
	print(data)

	return render(request,'View_Appointments.html',{'data':data})


def Booking_status(request,id):
	Appointment.objects.all().filter(id = id).update(Appointment_Status = "Accepted")

	Doctor_id = request.session['UserId']
	data = Appointment.objects.all().filter(Doctor = Doctor_id)
	print(data)

	return render(request,'View_Appointments.html',{'data':data})	

def Booking_status1(request,id):
	Doctor_id = request.session['UserId']
	Appointment.objects.all().filter(id = id).update(Appointment_Status = "Rejected")
	data = Appointment.objects.all().filter(Doctor = Doctor_id)
	print(data)

	return render(request,'View_Appointments.html',{'data':data})



def Give_Treatment(request,id):
	print(id)
	data = Appointment.objects.all().filter(id = id)


	return render(request,"Give_Treatment.html",{'data':data})


def Treatment(request):
	if request.method == "POST":
		b_id = request.POST['b_id']
		d_name = request.POST['d_name']
		Reason = request.POST['Reason']
		Medical_History = request.POST['Medical_History']
		Reason = request.POST['Reason']
		Medical_History = request.POST['Medical_History']
		Prescription = request.POST['Prescription']
		Diagnosis = request.POST['Diagnosis']
		Follow_Up_Instructions = request.POST['Follow_Up_Instructions']
		Lab_Tests = request.POST['Lab_Tests']
		Billing_and_Payment = request.POST['Billing_and_Payment']
		Appointment.objects.all().filter(id = b_id).update(Prescription = Prescription,Diagnosis =Diagnosis ,Follow_Up_Instructions = Follow_Up_Instructions,Lab_Tests = Lab_Tests,Billing_and_Payment = Billing_and_Payment,Treatment_Status = "Given")
		return redirect('/View_Appointments')
	else:
		return redirect('/View_Appointments')


def pay_doctor(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('modalid')
        doctor_fee = request.POST.get('modalfee')
        card_number = request.POST.get('cardNumber')
        expiration_date = request.POST.get('expirationDate')
        cvv = request.POST.get('cvv')
        
        # Update the payment status in the appointment table
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.Fee_status = 'Paid'
        appointment.save()
        messages.success(request, 'Payment Done Successfully')
        
        # Redirect to a success page or any other relevant page
        return redirect('/User_Appointments')  # Update 'success_page' to the desired URL
    else:
    	return redirect('/User_Appointments')


def View_User(request):
	details = UserDetails.objects.all()
	return render(request,"View_User.html",{'details':details})


def Submit_User_Feedback(request):
	if request.method == "POST":
		user = request.session['UserId']
		feedback = request.POST['feedback']

		obj = User_Feedback(user=user,feedback=feedback)
		obj.save()
		messages.info(request,"Feedback Submitted")
		return redirect('/Submit_User_Feedback/')
	else:
		user = request.session['UserId']
		details = User_Feedback.objects.filter(user=user)
		return render(request,"Submit_User_Feedback.html",{'details':details})


def Feedback(request):
	if request.method == "POST":
		user = request.session['UserId']
		feedback = request.POST['feedback']

		obj = Doctor_Feedback(doctor=user,feedback=feedback)
		obj.save()
		messages.info(request,"Feedback Submitted")
		return redirect('/Feedback/')
	else:
		user = request.session['UserId']
		details = Doctor_Feedback.objects.filter(doctor=user)
		return render(request,"Feedback.html",{'details':details})


def View_Doctor_Feedback(request):
	details = Doctor_Feedback.objects.all()
	return render(request,"View_Doctor_Feedback.html",{'details':details})

def View_User_Feedback(request):
	details = User_Feedback.objects.all()
	return render(request,"View_User_Feedback.html",{'details':details})


def Reply_Doctor(request,id):
	if request.method == "POST":
		reply = request.POST['reply']
		Doctor_Feedback.objects.filter(id=id).update(response=reply)
		messages.info(request,"Replied")
	return redirect('/View_Doctor_Feedback/')

def Reply_User(request,id):
	if request.method == "POST":
		reply = request.POST['reply']
		User_Feedback.objects.filter(id=id).update(response=reply)
		messages.info(request,"Replied")
	return redirect('/View_User_Feedback/')


def Logout(request):
	Session.objects.all().delete()
	return redirect("/")
