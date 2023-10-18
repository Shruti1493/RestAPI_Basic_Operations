from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Address = models.CharField(max_length=500)
    JOB = models.CharField(max_length=100)
    Salary = models.IntegerField()

    def __str__(self):
        return self.Name
    

