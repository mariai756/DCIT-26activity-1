from django.urls import path
from .views import HomePageView, AboutPageView, HobbiePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('hobbie/', HobbiePageView.as_view(),name= 'hobbie')
]