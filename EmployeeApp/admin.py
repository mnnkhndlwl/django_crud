from django.contrib import admin
from .models import Employees,Departments,User

# Register your models here.
admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(User)

