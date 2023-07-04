from . import views

from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', auth_views.LoginView.as_view(), name='logout')
]
