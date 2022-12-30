from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone_number=models.PositiveIntegerField()

    def __str__(self):
        return self.name


# Create your models here.
