from django.db import models

# Create your models here.

class Status(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title

class Employee(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
       return self.name 



class New_Lead(models.Model):
    site = models.CharField(max_length=200, null=True)
    cont_person = models.CharField(max_length=200, null=True)
    cont_no = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True)
    started = models.DateTimeField(null=True)
    expected = models.DateTimeField(null=True)
    verified = models.DateTimeField(null=True)
    action = models.DateTimeField(null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    lead_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.site

class Users(models.Model):
    Firstname = models.CharField(max_length=200, null=True)
    Lastname = models.CharField(max_length=200, null=True)
    UserEmail = models.EmailField(max_length=200, null=True)        
    
    def __str__(self):
        return self.Firstname + ' ' + self.Lastname

class JobCart(models.Model): 
    fullname = models.CharField(max_length=200, null=True)
    id_no = models.CharField(max_length=200, null=True)
    job_type = models.CharField(max_length=13, null=True)
    job_description = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.job_type


class New_Project(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True)
    started = models.DateTimeField(null=True)
    expected = models.DateTimeField(null=True)
    verified = models.DateTimeField(null=True)
    action = models.DateTimeField(null=True)
    site = models.CharField(max_length=200, null=True)
    cont_person = models.CharField(max_length=200, null=True)
    cont_no = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    lead_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.site    



class Dawn_Dusk(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title


class PPR(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title

class PPL(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title

class MAR(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title     

class DCI(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title            

class SS(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title  

class OI(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title         

class New_Validation(models.Model):
    
    site = models.CharField(max_length=200, null=True)
    cont_person = models.CharField(max_length=200, null=True)
    cont_no = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    solution_type = models.CharField(max_length=200, null=True)
    est_duration = models.CharField(max_length=200, null=True)
    ppr = models.ForeignKey(PPR,on_delete=models.CASCADE, null=True)
    ppl = models.ForeignKey(PPL,on_delete=models.CASCADE, null=True)
    mar = models.ForeignKey(MAR,on_delete=models.CASCADE, null=True)
    est_municipal = models.CharField(max_length=200, null=True)
    pce = models.CharField(max_length=200, null=True)
    dawn_dusk = models.ForeignKey(Dawn_Dusk,on_delete=models.CASCADE, null=True)
    dci = models.ForeignKey(DCI,on_delete=models.CASCADE, null=True)
    ss = models.ForeignKey(SS,on_delete=models.CASCADE, null=True)
    esc = models.CharField(max_length=200, null=True)
    oi = models.ForeignKey(OI,on_delete=models.CASCADE, null=True)
    lead_image = models.ImageField(null=True, blank=True, upload_to="images/")


