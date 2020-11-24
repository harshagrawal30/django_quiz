from django.db import models

# Create your models here.

class que(models.Model):
    pub_date = models.DateTimeField('date published')
    end_date=models.DateTimeField('Date Expired',default=None)
    Class=models.IntegerField()
  
    question_text = models.CharField(max_length=200)

    maths=models.BooleanField(default=False)
    biology=models.BooleanField(default=False)
    science=models.BooleanField(default=False)
    chemistry=models.BooleanField(default=False)
    physics=models.BooleanField(default=False)
    def __str__(self):
        return self.question_text
class choice(models.Model):
    question = models.ForeignKey(que, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_ans=models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text