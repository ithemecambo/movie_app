from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='movie'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]