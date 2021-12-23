from . import views
from django.urls import path
#app url
urlpatterns = [
    path('',views.home, name="home"),
    path('password',views.password, name="password"),
    path('about',views.about, name="about"),
]