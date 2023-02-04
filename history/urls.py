from django.urls import path
from . import views

urlpatterns = [
    path('',views.history,name='history'),
    path('delete/<str:id>/',views.delete,name='delete'),
]
