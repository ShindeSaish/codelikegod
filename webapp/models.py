from django.db import models

# Create your models here.
class Signin(models.Model):
    name = models.CharField(max_length=100, null=True)
    email =models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    conf = models.CharField(max_length=100, null=True)
    userPass = models.JSONField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    cname = models.CharField(max_length=100, null=True)
    cemail =models.CharField(max_length=100, null=True)
    csubject = models.CharField(max_length=100, null=True)
    cdisc = models.CharField(max_length=500, null=True)
    def __str__(self):
        return f'{self.cname} - {self.cdisc}'


