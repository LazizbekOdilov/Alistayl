from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('bolimlar/', BolimlarView.as_view(), name="bolimlar"),
    path('bolim/<int:pk>/', MahsulotlarView.as_view(), name="mahsulotlar"),
    path('mahsulot/<int:pk>/', MaahsulotView.as_view(), name="mahsulot"),
]