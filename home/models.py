from django.db import models
# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500,default="")
    email=models.CharField(max_length=300,default="")
    desc=models.CharField(max_length=4000,default="")
    phone=models.IntegerField(default=0)
    def __str__(self):
        return self.name
