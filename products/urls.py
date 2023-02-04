from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('productdetail/<str:id>/',views.viewProduct,name="viewProduct"),
    path('bookdate/<str:pk>/',views.bookdate,name="bookdate"),
    path('cancel-order/<str:pk>/',views.CancelOrder,name="CancelOrder"),
    path('search/',views.search,name='search'),
    path('history/',views.history,name='history'),
]
