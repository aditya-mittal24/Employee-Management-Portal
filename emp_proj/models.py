from django.db import models

# Create your models here.

class Department(models.Model):
    dept = models.CharField(max_length=30)
    
    def __str__(self):
        return self.dept
    
class Gender(models.Model):
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.gender

class Employee(models.Model):
    emp_id = models.CharField(max_length=12, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=10)
    email = models.EmailField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.BigIntegerField()
    position = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name