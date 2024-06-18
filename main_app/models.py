from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exams(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,related_name="Donors")
    name = models.CharField(max_length=100 ,  default = "")
    course = models.CharField(max_length=100)
    Exam_Type = models.CharField(max_length=100)
    Difficulty_Level= models.CharField(max_length=100)
    questions = models.CharField(max_length=10000 , default = "")
    answers = models.CharField(max_length = 1000 , default = "")
    def __str__(self):
        try:
            return f'{self.user.username} '
        except:
            pass


class Context(models.Model):
    course = models.CharField(max_length=100)
    data = models.CharField(max_length=100000)

    