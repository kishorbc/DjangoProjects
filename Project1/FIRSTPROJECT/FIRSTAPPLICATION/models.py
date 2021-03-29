from django.db import models

# Create your models here.


class Student(models.Model):
    Name = models.CharField(max_length=25)
    ID = models.IntegerField(primary_key=True)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Teacher(models.Model):
    Name = models.CharField(max_length=25)
    ID = models.IntegerField(primary_key=True)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Staff(models.Model):
    Name = models.CharField(max_length=25)
    ID = models.IntegerField(primary_key=True)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
