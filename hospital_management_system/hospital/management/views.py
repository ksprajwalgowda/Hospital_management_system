from django.shortcuts import render
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Patients,Doctor,Teatment,Medicine,Rooms
from django.urls import reverse_lazy
from .forms import AddPatientForm,AddTreatmentForm,AddMedicineForm
# Create your views here.


obj_doc_details = Doctor.objects.all()

def home(request):
    
    context = {
        "patient_no":Patients.objects.all().count(),
        "doctor_no":Doctor.objects.all().count(),
        "doc_details":obj_doc_details,
    }
    return render(request,"index.html",context)

def avlroom(request):
    obj = Rooms.objects.filter(avaliable = "yes")
    obj1 = Rooms.objects.filter(avaliable = "no")
    

    cont = {
        "avlrooms" : obj,
        "filledroom":obj1,
        
    }

    return render(request,"rooms.html",cont)




class updateRoom(UpdateView):
    model = Rooms
    fields = [ 
        "avaliable",
        "pname"
        
    ]
    template_name = "updateroom.html"
    success_url ="/management/rooms/"

class PatientView(ListView):
    model = Patients 
    template_name = "patient.html"

class DoctorView(ListView):
    model =  Doctor
    template_name = "doc.html"

class AddPatient(CreateView):
    module = Patients
    template_name = "addpatient.html"
    form_class = AddPatientForm
    success_url = reverse_lazy('management:patientsDetails')

class updatePatient(UpdateView):
    model = Patients
    fields = "__all__"
    template_name = "updatepatient.html"
    success_url ="/management/patient/"

class TeatmentListView(ListView):
    model = Teatment
    template_name = "treatment.html"

class AddTreatment(CreateView):
    module = Teatment
    template_name = "addpatient.html"
    form_class = AddTreatmentForm
    success_url = reverse_lazy('management:treatmentview')

class Medicine(ListView):
    model = Medicine
    template_name = "medicine.html"

class AddMedicine(CreateView):
    module = Medicine
    template_name = "addmedicine.html"
    form_class = AddMedicineForm
    success_url = reverse_lazy('management:medicine')

class updateTreatment(UpdateView):
    model = Teatment
    fields = "__all__"
    template_name = "updatetreatment.html"
    success_url ="/management/treatment/"

# class updateMedicine(UpdateView):
#     model = Medicine
#     fields = "__all__"
#     template_name = "updatemedicine.html"
#     success_url ="/management/medicine/"

class deletepatient(DeleteView):
    model = Patients
    template_name = "deletepatient.html"
    success_url ="/management/patient/"

class deleteTreatment(DeleteView):
    model = Teatment
    template_name = "deletetreatment.html"
    success_url ="/management/treatment/"

# class deletemedicine(DeleteView):
#     model = Medicine
#     template_name = "deletemedicine.html"
#     success_url ="/management/medicine/"


