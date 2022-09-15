from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    phone_no = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    addressDetails = models.CharField(max_length=200)
    home_no = models.PositiveIntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    work_experience= models.IntegerField()
    company_name = models.CharField(max_length=50)
    from_date = models.IntegerField()
    to_date = models.IntegerField()
    address = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=50)
    qualifications_name= models.CharField(max_length=50)
    percentage = models.IntegerField()
    projects = models.CharField(max_length=100)
    title = models.CharField(max_length=40)
    descriptions = models.CharField(max_length=200)
    photo = models.ImageField()


