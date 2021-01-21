from django.urls import path,include
from .views import *
app_name = 'management'
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("patient/",PatientView.as_view(),name='patientsDetails' ),
    path("patient/<pk>/",updatePatient.as_view(),name= "updatepatient"),
    path("doctor/",DoctorView.as_view(),name='doctorDetails'),
    path("addpatient/",AddPatient.as_view(),name='addPatient'),
    path("treatment/",TeatmentListView.as_view(),name='treatmentview'),
    path("treatment/<pk>/",updateTreatment.as_view(),name="updatetreatment"),
    path("addtreatment/",AddTreatment.as_view(),name='addtreatment'),
    path("medicine/",Medicine.as_view(),name='medicine'),
    # path("medicine/<pk>/",updateMedicine.as_view(),name="updatemedicine"),
    path("addmedicine/",AddMedicine.as_view(),name='addmedicine'),
    path("rooms/",avlroom, name = 'rooms'),
    path('rooms/<pk>', updateRoom.as_view(),name='updateRoom'),
    path("patient/<pk>/delete/",deletepatient.as_view()),
    path("treatment/<pk>/delete/",deleteTreatment.as_view()),
    # path("medicine/<pk>/delete/",deletemedicine.as_view()),
    
]