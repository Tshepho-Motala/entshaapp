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
    

