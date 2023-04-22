from django.urls import path
from .views import homePage, AllCourse, Coursdetail

urlpatterns = [
    path('', homePage, name="home"),
    path('cours/', AllCourse, name="cours"),
    path('cours/<slug>', Coursdetail,name="cours"),

]

