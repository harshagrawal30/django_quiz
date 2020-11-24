from django.db import models

# Create your models here.
class user_res(models.Model):
    username=models.CharField(max_length=20)
    question_id=models.IntegerField(default=0)
    question_text=models.CharField(max_length=200)
    correct_ans=models.CharField(max_length=20)
    solved_c_n=models.BooleanField(default=False)
    solved=models.BooleanField(default=False)
    maths=models.BooleanField(default=False)
    biology=models.BooleanField(default=False)
    science=models.BooleanField(default=False)
    chemistry=models.BooleanField(default=False)
    physics=models.BooleanField(default=False)
