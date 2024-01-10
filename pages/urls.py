from django.urls import path
from .views import say_hello

#urlpattern
urlpatterns = [
    path('', say_hello)
]
