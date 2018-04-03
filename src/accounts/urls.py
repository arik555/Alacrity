from django.urls import path, include
from .views import login_user, register_user
urlpatterns = [
    path('login/', login_user, name="login"),
    # register_user
    path('register/', register_user, name="register"),
]