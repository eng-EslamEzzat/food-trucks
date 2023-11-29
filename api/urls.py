from django.urls import path, include
from .views import get_trucks

urlpatterns = [
    # retruns 5 trucks by default
    path('', get_trucks),

    # returns the number of trucks based on the pk
    path('<int:pk>', get_trucks),
]