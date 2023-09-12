from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('djangoapp/', views.djangoapp, name='djangoapp'),
    path('djangoapp/memberdetails/<int:id>', views.memberdetails, name='memberdetails'),
]