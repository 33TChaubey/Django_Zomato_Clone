from django.urls import path,include
from users import views

app_name = 'users'

urlpatterns = [
    path('orders/<int:itemid>/<int:pdcd>/<str:user>/',views.orders,name='Orders'),
    path('updateorders/<int:orderid>/<int:itemid>/',views.update_orders,name='updateorder'),
    path('crf/<int:itemid>/<int:pc>/', views.CusRatFeedView, name="crf"),
    path('updcrf/<int:detailid>/<int:crfid>/', views.UpdateCRF, name='updcrf'),
    # deleting customer ratings and feedbacks
    path('delcrf/<int:detailid>/<int:crfid>/', views.DeleteCRF, name='delcrf'),
        # paypal checkout button
    path('buy/<int:amt>/<int:qnt>/', views.Payment, name='buy'),
        # paypal on approve
    path('oa/', views.OnApprove, name='oa'),

    # paypal payment success
    path('ps/', views.PaymentSuccess, name='ps'),
    path('ps/<int:var>/', views.PaymentSuccessVar, name='psvar'),
    

]
