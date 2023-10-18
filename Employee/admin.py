from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAPI(admin.ModelAdmin):
    list_display = ['id','Name','Age','Address','JOB','Salary']