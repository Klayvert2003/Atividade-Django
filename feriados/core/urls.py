from django.urls import path
from . import views

urlpatterns = [
    path('',views.natal),
    path('tiradentes/', views.redireciona, name='tiradentes'),
    path('',views.tiradentes),
]