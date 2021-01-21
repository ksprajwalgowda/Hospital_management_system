from django import forms
from .models import Patients,Teatment,Medicine

class AddPatientForm(forms.ModelForm):
    class Meta():
        model = Patients
        fields = '__all__'

class AddTreatmentForm(forms.ModelForm):
    class Meta():
        model = Teatment
        fields = '__all__'

class AddMedicineForm(forms.ModelForm):
    class Meta():
        model = Medicine
        fields = '__all__'

