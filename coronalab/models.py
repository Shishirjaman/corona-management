from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RegUser(models.Model):
    user = models.OneToOneField(User,null=True,on_delete= models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True,blank=True,default="not added")
    email = models.CharField(max_length=200,null=True, blank=True)
    address = models.CharField(max_length=200,null=True,blank=True,default="not added")
    
    def __str__(self):
        return self.name


class TestCenter(models.Model):
    name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    noOftest = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    STATUS = (
    ('pending','pending'),
    ('positive','positive'),
    ('negative','negative'),
    )
    user = models.ForeignKey(RegUser,null=True,on_delete=models.CASCADE)
    testcenter = models.ForeignKey(TestCenter,null=True,on_delete=models.CASCADE)
    date = models.DateField(null=True)
    status = models.CharField(max_length=100,blank=True,null=True,choices=STATUS, default="pending")
    
    def __str__(self):
        return self.user.name

class WorldUpdate(models.Model):
    dailytotaltest = models.IntegerField(null=True)
    dailypositive = models.IntegerField(null=True)
    dailyrecoverd = models.IntegerField(null=True)
    dailydeath = models.IntegerField(null=True)
    date = models.DateField(null=True)

class BangladeshUpdate(models.Model):
    dailytotaltest = models.IntegerField(null=True)
    dailypositive = models.IntegerField(null=True)
    dailyrecoverd = models.IntegerField(null=True)
    dailydeath = models.IntegerField(null=True)
    date = models.DateField(null=True)
    
    
