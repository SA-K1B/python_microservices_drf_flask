from django.urls import path
from .views import home
urlpatterns = [
    path('<str:name>',home,name = "home"),
]