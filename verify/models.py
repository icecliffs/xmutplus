from django.db import models

# Create your models here.
class Students(models.Model):
    realname = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)