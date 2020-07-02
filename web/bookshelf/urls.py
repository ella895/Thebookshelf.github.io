from django.urls import path
from . import views
from bookshelf import views
from .views import mt

urlpatterns = [
    path('',views.index,name='index'),
    path('contacts/',views.contacts,name='contacts'),
    path('team/',views.team,name='team'),
    path('mt/<int:id>/',views.mt,name='mt'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('register/',views.register,name='register')]