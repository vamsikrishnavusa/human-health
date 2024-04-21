from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
				path('',views.Home,name="Home"),
				path('Admin_Login/',views.Admin_Login,name="Admin_Login"),
				path('User_Login/',views.User_Login,name="User_Login"),
				path('Doctor_Login/',views.Doctor_Login,name="Doctor_Login"),
				path('User_Registration/',views.User_Registration,name="User_Registration"),
				path('Prediction/',views.Prediction,name="Prediction"),
				path('Manage_Doctor/',views.Manage_Doctor,name="Manage_Doctor"),
				path('Add_Doctor/',views.Add_Doctor,name="Add_Doctor"),
				path('Doctor_Registration/',views.Doctor_Registration,name="Doctor_Registration"),
				path('Doctor_Edit_Profile/',views.Doctor_Edit_Profile,name="Doctor_Edit_Profile"),
				path('View_Doctor/<int:id>',views.View_Doctor,name="View_Doctor"),
				path('Accept/<int:id>',views.Accept,name="Accept"),
				path('BookAppointment/<str:name>',views.BookAppointment,name="BookAppointment"),
				path('Book_doctor/<int:id>',views.Book_doctor,name="Book_doctor"),
				path('BookAppointments/',views.BookAppointments,name="BookAppointments"),
				path('User_Appointments/',views.User_Appointments,name="User_Appointments"),
				path('View_Appointments/',views.View_Appointments,name="View_Appointments"),
				path('Booking_status/<int:id>',views.Booking_status,name="Booking_status"),
				path('Booking_status1/<int:id>',views.Booking_status1,name="Booking_status1"),
				path('Give_Treatment/<int:id>',views.Give_Treatment,name="Give_Treatment"),
				path('Treatment/',views.Treatment,name="Treatment"),
				path('pay_doctor/',views.pay_doctor,name="pay_doctor"),
				path('View_User/',views.View_User,name="View_User"),
				path('Submit_User_Feedback/',views.Submit_User_Feedback,name="Submit_User_Feedback"),
				path('Feedback/',views.Feedback,name="Feedback"),
				path('View_Doctor_Feedback/',views.View_Doctor_Feedback,name="View_Doctor_Feedback"),
				path('Reply_Doctor/<int:id>',views.Reply_Doctor,name="Reply_Doctor"),
				path('Reply_User/<int:id>',views.Reply_User,name="Reply_User"),
				path('View_User_Feedback/',views.View_User_Feedback,name="View_User_Feedback"),
				path('Logout/',views.Logout,name="Logout"),
				

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

