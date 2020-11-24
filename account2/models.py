from django.db import models

# Create your models here.
class user_info(models.Model):
    username=models.CharField(max_length=20)
    username1=models.CharField(max_length=20,default='')
    password1=models.CharField(max_length=15)
    password2=models.CharField(max_length=15)
    classnum=models.IntegerField()
    Total_Question_faced=models.IntegerField(default=0)

