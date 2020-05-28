from django.db import models
from account.models import Account
class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    surname = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100,null=True)
    patronymic = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=12,null=True)
    birth_date = models.DateField(auto_now=False,null=True)
    start_study_date = models.DateField(auto_now=False, null=True)
    specialization = models.CharField(max_length=200, null=True)
    group = models.CharField(max_length=50, null=True)
    skills = models.TextField(max_length=300, null=True)
    
    
