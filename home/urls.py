from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search', views.Search, name="search"),
    path('signup',views.handleSignUp,name="signup"),
    path('login',views.handleLogin,name="Login"),
    path('logout',views.handleLogout,name="Logout")
]