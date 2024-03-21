from django.contrib import admin
from food.models import Item,History, NavbarFrom

# Register your models here.

class DetailViewIndex(admin.ModelAdmin):
    list_display = ['rest_owner', 'prod_code', 'item_name']
    
class HistoryDetailView(admin.ModelAdmin):
    list_display = ['username', 'prod_code', 'item_name','operation_type','user_type']
    
    
admin.site.register(Item,DetailViewIndex)
admin.site.register(History,HistoryDetailView)
admin.site.register(NavbarFrom)


