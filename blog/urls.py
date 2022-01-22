from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.homeBlog,name="homeBlog"),
    path('postComment', views.postComment, name="postComments"),
    path('<str:slug>/',views.blogpost,name="blogpost"),

]