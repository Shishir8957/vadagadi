from django.urls import path
from . import views

urlpatterns = [
    path('',views.register, name='register'),
    path('signin',views.register, name='register'),
    # path('',views.login, name='register'),
    path('activateUser/<str:slug>/',views.activateUser, name='activateUser'),
    path('password_reset/',views.password_reset, name='password_reset'),
    path('password_reset/email_submited',views.email_submited, name='email_submited'),
    path('password_reset/<str:slug>/',views.userValid, name='userValid'),
    path('password_reset/<str:slug>/update_password',views.update_password, name='update_password'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('search/<str:slug>/',views.search,name='search'),
    path('user-profile/',views.userprofile,name='userprofile'),
    path('user-profile/<str:id>/',views.userprofileUpdate,name='userprofileUpdate'),
]