from django.urls import path
from .views import *

urlpatterns = [
    path('buyurtma/', TanlanganView.as_view(), name="buyurtma"),
    path('buyurtmalar/', BuyurtmalarView.as_view(), name="buyurtmalar"),
    path('savatlar/', SavatlarView.as_view(), name="savatlar"),
]