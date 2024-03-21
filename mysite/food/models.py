from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    rest_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(
        max_length=500,
        default="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas ad quos, aliquid enim omnis expedita porro aut exercitationem adipisci id perspiciatis fugiat consectetur aliquam consequuntur sapiente hic vitae unde! Possimus."
    )
    
    prod_code = models.IntegerField(default=50)
    added_by=models.CharField(
        max_length=50,
        default='user'
    )
    
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://th.bing.com/th/id/R.e826020767e491f4054f6fcfd6d44222?rik=Fs2Mp4uA96SBRw&riu=http%3a%2f%2fwww.fnasafety.com%2fwp-content%2fuploads%2f2016%2f04%2fComingSoon2-fnasafety.png&ehk=qk9WvOpnJXmBGGVNzXXCziDdKvkr5eyyukPFh2SdZe4%3d&risl=&pid=ImgRaw&r=0"
    )
    
    def __str__(self):
        return str(
            (   self.item_name,
                self.prod_code,
                self.rest_owner
            )
        )

class History(models.Model):
    
    username = models.CharField(max_length=100)
    prod_code = models.IntegerField()
    item_name = models.CharField(max_length=100)
    operation_type = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    def __str__(self):
        return str(
            (
                self.username ,
                self.prod_code,
                self.item_name,
                self.operation_type
            )
        )
    
class NavbarFrom(models.Model):
    data = models.CharField(max_length=100) 
    
    
    def __str__(self):
        return str(
            self.data
        )  