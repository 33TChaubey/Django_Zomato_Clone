from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile, CusOrders, CusRatingFeedback

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name  = forms.CharField()
    last_name = forms.CharField()    
    
    class Meta:
        model = User
        fields = ['username',  'email' ,'first_name', 'last_name', 'password1', 'password2']
        
class ProfFormEditing(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['user' ,'image', 'location', 'user_type']
        
        
#Profile Form Two

class ProfFormCreating(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user' ,'image', 'location', 'user_type']
        
class Updateorder(forms.ModelForm):
    class Meta:
        model = CusOrders
        fields = ['quantity']
        

class CusRatFeedForm(forms.ModelForm):
    class Meta:
        model = CusRatingFeedback
        fields = ['ratings', 'feedback']