from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name="register"),
    path('tasdiqlash/', Kod_Tasdiqlash.as_view(), name="kod_tasdiqlash"),
]