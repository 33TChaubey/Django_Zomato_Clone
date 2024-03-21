from django.contrib import admin
from users.models import Profile, ItemPictures, CusOrders, CusRatingFeedback

# Register your models here.


admin.site.register(Profile)
admin.site.register(ItemPictures)
admin.site.register(CusOrders)
admin.site.register(CusRatingFeedback)


