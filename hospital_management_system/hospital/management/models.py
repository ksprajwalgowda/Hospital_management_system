from django.db import models

# Create your models here.
class Doctor(models.Model):
   
    firstName = models.CharField(max_length=50,null=False,verbose_name = "First name")
    lastName = models.CharField(max_length=50,null=False,verbose_name = "Last name")
    did = models.PositiveIntegerField(null=False,unique=True,default=1,verbose_name = "Doctor ID")
    qualification = models.CharField(max_length=50,null=False,verbose_name = "Qualification")
    email = models.CharField(max_length=50,default="NULL")
    specialization = models.CharField(max_length=50,null=True,verbose_name = "Specialization")
    address = models.CharField(max_length=50,null=False,verbose_name = "Address") 
    phNo = models.CharField( max_length=10,verbose_name = "Phone Number")
    experince = models.IntegerField(verbose_name = "Experince")

    def __str__(self):
        return self.firstName


class Patients(models.Model):
    # id = models.IntegerField(primary_key=True,default=1)
    firstName = models.CharField(max_length=50,null=False,verbose_name = "First name")
    lastName = models.CharField(max_length=50,null=False,verbose_name = "Last name")
    email = models.EmailField(max_length=254)
    pid = models.PositiveIntegerField(null=False,unique=True,default=1,verbose_name = "Patient ID")
    bloodGroup = models.CharField(max_length=3,null=False,verbose_name = "Blood Group")
    age = models.PositiveIntegerField(verbose_name = "Age")
    address = models.CharField(max_length=50,null=False,verbose_name = "Address") 
    phNo = models.CharField( max_length=10,verbose_name = "Phone Number")
    # doc = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.firstName



class Teatment(models.Model):
    
    tid = models.CharField(max_length=50,null = False,unique=True,verbose_name = "Treatment ID")
    pname = models.ForeignKey(Patients, on_delete=models.CASCADE,verbose_name = "Patient Name")
    dname = models.ForeignKey(Doctor, on_delete=models.CASCADE,verbose_name = "Doctor Name")
    description = models.TextField(verbose_name = "Description")

    def __str__(self):
        return self.tid


class Medicine(models.Model):
    
    mno = models.CharField(max_length=50,null = False,unique=True,verbose_name = "Medicine ID")
    mname = models.CharField(max_length=50,null=False,verbose_name = "Medicine Name")
    quantity = models.PositiveIntegerField(null=False,verbose_name = "Quantity")
    price = models.CharField(max_length=50,null=False,verbose_name = "Price")
    pname = models.ForeignKey(Patients, on_delete=models.CASCADE,verbose_name = "Patient Name")
    def __str__(self):
        return self.mno



class Rooms(models.Model):
    
    roomNo = models.CharField(max_length=50,null=False,unique=True,verbose_name = "Room Number")
    rtype = models.CharField( max_length=50,null=False,verbose_name = "Room Type")
    rent = models.PositiveIntegerField(null=False,verbose_name = "Rent")
    pname = models.ForeignKey(Patients, on_delete=models.CASCADE,null = True,default="null",verbose_name = "Patient Name")
    yes_no = (
        ("yes","yes"),
        ("no","no")
    )
    avaliable = models.CharField( max_length=50,choices = yes_no,default = "yes",verbose_name = "Avaliable")

    def __str__(self):
        return self.roomNo
