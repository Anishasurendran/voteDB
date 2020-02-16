from django.db import models

# Create your models here.


class TempData(models.Model):
    aadhar = models.CharField(max_length=12,default=None, blank=True, null=True)
    dob = models.DateField(default=None)
    gender = models.CharField(default=None, max_length=1)
    name = models.CharField(default=None, max_length=25)
    careof = models.CharField(default=None, max_length=25)
    dist = models.CharField(default=None, max_length=36)
    address = models.CharField(default=None, max_length=256)
    pin = models.CharField(default=None, max_length=7)

    def __str__(self):
        return str(self.name)
