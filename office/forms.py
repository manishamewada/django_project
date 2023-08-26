from django import forms
from . models import Employee,Role,Department

class AddData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    phone=models.IntegerField(default=0)
    role=models.CharField(max_length=100)
    dept_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    hire_date=models.IntegerField(default=0)