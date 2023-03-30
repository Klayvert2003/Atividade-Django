from django.urls import path
from . import views

urlpatterns = [
    path('',views.natal, name='natal'),
    path('tiradentes/', views.tiradentes, name='tiradentes'),
]