from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('productdetail/<str:id>/',views.viewProduct,name="viewProduct")
]
