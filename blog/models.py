from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500,default="")
    content=models.TextField()
    author=models.CharField(max_length=4000,default="")
    slug=models.CharField(max_length=130,default="")
    phone=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    def __str__(self):
        return self.title
class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:10]+"..."+"by "+self.user.username
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="customer")
    address=models.CharField(max_length=23434,default="")
    
