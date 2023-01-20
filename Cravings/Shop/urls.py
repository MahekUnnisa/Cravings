from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='Home'),
    path('about',views.about,name='AboutUs'),
    path('contact',views.contact,name='ContactUs'),
    path('recepies',views.recepies,name='Recepies'),
    path('test',views.test,name='Test'),
    path('menu',views.menu,name='Menu'),
    path('login',views.login,name='Login'),
    path('signup',views.signup,name='Signup'),
    path('logout',views.logout,name='Logout'),
]