from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patients)
admin.site.register(Doctor)
admin.site.register(Teatment)
admin.site.register(Medicine)
admin.site.register(Rooms)