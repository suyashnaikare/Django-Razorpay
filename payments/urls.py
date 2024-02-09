from django.urls import path ;
from payments import views

urlpatterns = [
     path('',views.pay_page,name='payment'),
     path('payment/',views.create_order,name='createorder'),
     
]
