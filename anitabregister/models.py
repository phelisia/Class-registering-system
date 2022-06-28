from django.db import models

# Create your models here.


class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  studentcode=models.IntegerField(max_length=255)
  lab=models.CharField(max_length=255)
  # email=models.CharField(max_length=200)
  