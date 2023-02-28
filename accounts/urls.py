from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_account, name='signup'),
    path('login/', views.login_account, name='login'),
    path('logout/', views.logout_account, name='logout'),
]

