from django import forms
from food.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['prod_code','rest_owner' ,'item_name', 'item_desc', 'item_price', 'item_image']
        

