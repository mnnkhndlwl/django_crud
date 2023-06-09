from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

    def __str__(self):
      return self.name + ' ' + self.description

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

    def __str__(self):
      return self.EmployeeName

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)

    def __str__(self):
      return self.username