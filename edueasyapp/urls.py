from django.contrib import admin
from django.urls import path
from edueasyapp import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('aboutus', views.about, name='aboutpage'),
    path('contactus', views.contact, name='contact'),
    path('courses', views.course, name='course'),
    path('resources', views.resource, name='resource'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('pythonforbeginners', views.python, name='python'),
    path('register', views.sign, name='sign'),
    path('loguser', views.loguser, name='loguser'),
    path('edueasy', views.main, name='main'),
]