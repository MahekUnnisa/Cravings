from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='Home'),
    path('about',views.about,name='AboutUs'),
    path('contact',views.contact,name='ContactUs'),
    path('recepies',views.recepies,name='Recepies'),
    path('test',views.test,name='Test'),
]