from django.db import models

# Create your models here.


class user(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    # email = models.EmailField()
    # password = models.CharField(max_length=30, default=None)
    date = models.DateField()
    gender = models.CharField(max_length=10)


class login(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)


class esample(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    date = models.DateField(default=None)
    gender = models.CharField(max_length=10, default=None)


class sample2(models.Model):
    imagename = models.CharField(max_length=30)
    filename = models.CharField(max_length=40)


class sample3(models.Model):
    name = models.CharField(max_length=30)
    contact = models.BigIntegerField()
    place = models.CharField(max_length=30)
