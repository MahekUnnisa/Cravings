from . import views
from django.urls import path,include
urlpatterns=[
    path('',views.index,name='Home'),
    path('test',views.test,name='Test'),
    path('recepies',views.recepies,name='Recepies'),
]