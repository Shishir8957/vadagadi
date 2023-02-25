from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('category/cars/',views.car,name="car"),
    path('category/price/',views.price,name="price"),
    path('category/name/',views.name,name="name"),
    path('category/bikes/',views.bike,name="bike"),
    path('productdetail/<str:id>/',views.viewProduct,name="viewProduct"),
    path('bookdate/<str:pk>/',views.bookdate,name="bookdate"),
    path('cancel-order/<str:pk>/',views.CancelOrder,name="CancelOrder"),
    path('complete-order/<str:pk>/',views.CompleteOrder,name="CompleteOrder"),
    path('search/',views.search,name='search'),
    path('history/',views.history,name='history'),
    path('payment/',views.payment,name="payment"),
    path('postComment',views.postComment,name="postComment"),
    path('deleteComment/<str:slug>',views.deleteComment,name="deleteComment"),
]
