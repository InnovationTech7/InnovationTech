from django.urls import path
from .views import user_login, user_logout, register
urlpatterns = [
    path('inscription', register, name="login"),
    path('connexion', user_login, name="login"),
    path('deconnexion', user_logout, name="logout")
]
