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



class Public_PR(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title 

class Public_P(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title  

class Municipality(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title                     

class Interest(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title

class Shareable(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title  

class Operator(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title   

class Months(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
       return self.title                


class New_Validation(models.Model):

    site = models.CharField(max_length=200, null=True)
    cont_person = models.CharField(max_length=200, null=True)
    cont_no = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    solution = models.CharField(max_length=200, null=True)
    duration_ppr = models.CharField(max_length=200, null=True)
    public_pr = models.ForeignKey(Public_PR,on_delete=models.CASCADE, null=True)
    public_p = models.ForeignKey(Public_P,on_delete=models.CASCADE, null=True)
    municapal_approval = models.ForeignKey(Municipality,on_delete=models.CASCADE, null=True)
    est_municipal = models.CharField(max_length=200, null=True)
    power_connection = models.CharField(max_length=200, null=True)
    dusk_dawn = models.ForeignKey(Months,on_delete=models.CASCADE, null=True)
    del_connect_interest = models.ForeignKey(Interest,on_delete=models.CASCADE, null=True)
    solution_share = models.ForeignKey(Shareable,on_delete=models.CASCADE, null=True)
    Operator_interest = models.ForeignKey(Operator,on_delete=models.CASCADE, null=True)
    lead_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.site          
    

