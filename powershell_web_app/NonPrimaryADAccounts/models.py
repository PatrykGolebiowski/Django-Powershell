from django.db import models

# Create your models here.

class NonPrimaryADAccount(models.Model):
    PrimaryID = models.CharField(max_length=30)
    SecondaryID = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    EmailAddress = models.EmailField(max_length=200)
    JobTitle = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    Company = models.CharField(max_length=200)
    Manager = models.CharField(max_length=200)
    ManagerID = models.CharField(max_length=30)
    CreatedAt = models.DateField()