from django.urls import path,include
from food import views
from users import views as userviews

app_name = 'food'

urlpatterns = [
    
    
    
    #function based index views
    #----------------------------------------------------------------------------
    path('home/',views.index,name='index'),
    
    #class based index views
    #----------------------------------------------------------------------------
    #path('home/',views.IndexClassView.as_view(),name='index'),
    
    
    #function based detail views
    #----------------------------------------------------------------------------
    path('detail/<int:item_id>/',views.detail,name='detail'),
    
    #function based detail views
    #----------------------------------------------------------------------------
    #path('detail/<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    
    #function based create_item views
    #----------------------------------------------------------------------------
    path('add/',views.create_item,name='create_item'),
    
    #class based create_item views
    #----------------------------------------------------------------------------
    #path('add/',views.CreateItem.as_view(),name='create_item'),
    
    
    #function based update_item views
    #----------------------------------------------------------------------------
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    
    #function based delete_item views
    #----------------------------------------------------------------------------
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),
    
    #Navbar Form View
    #-------------------------------------------------------------------

    path('navform/',views.NavForm, name='navform')
    
    
]
