from django.urls import path
from .views import say_hello, HomePageView, AboutPageView

#urlpattern
urlpatterns = [
    path('hello/', say_hello),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name='home')
]
