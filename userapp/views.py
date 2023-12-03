from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .models import Profil
import random
# from eskiz.client import SMSClient
class LoginView(View):
    def get(self, request):
        return render(request, "page-user-login.html")

class RegisterView(View):
    def get(self, request):
        return render(request, "page-user-register.html")

    def post(self, request):
        profil = Profil.objects.create_user(
            username= request.POST.get("t"),
            password = request.POST.get("p"),
            tel = request.POST.get("t"),
            first_name = request.POST.get("f"),
            last_name = request.POST.get("l"),
            davlat = request.POST.get("d"),
            shahar = request.POST.get("sh"),
            jins = request.POST.get("gender"),
            tasdiqlash_kod = str(random.randrange(10000, 100000))
        )
        mijoz = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email=settings.ESKIZ_GMAIL,
            password=settings.ESKIZ_PAROL,
        )

        mijoz._send_sms(
            phone_number=profil.tel,
            message=f"Alistyl loyihasidagi tasdiqlash kodingiz: "
                    f"           {profil.tasdiqlash_kod}           "

        )
        return redirect("/user/tasdiqlash/")




class Kod_Tasdiqlash(View):
    def get(self, request):
        return render(request, "kod_tasdiqlash.html")