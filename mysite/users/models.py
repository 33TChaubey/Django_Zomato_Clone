from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    user  =  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(default='location',max_length=100)
    user_type = models.CharField(max_length=200, default="user_type")
    
    
    def __str__(self):
        return self.user.username


class ItemPictures(models.Model):
    name = models.CharField(max_length=255, default='itemname')
    pic = models.ImageField(default='itempic.jpg',upload_to='item_pictures')
    
    def __str__(self):
        return self.name
    

class CusOrders(models.Model):

    order_id = models.AutoField(primary_key=True)
    prod_code = models.IntegerField()
    quantity = models.IntegerField(default=1)
    username = models.CharField(max_length=200)

    def __str__(self):
        return str(
            (
                str(self.order_id),
                str(self.prod_code),
                str(self.quantity),
                str(self.username)
            )
        )
        
class CusRatingFeedback(models.Model):
    prod_code = models.IntegerField(default=1)
    ratings = models.FloatField(default=0.0)
    feedback = models.TextField(max_length=500, default='feedback')
    username = models.CharField(max_length=200,default='username')
    
    
    def __str__(self):
        return str(
            (
                self.prod_code,
                self.ratings,
                self.feedback,
                self.username
            )
        )