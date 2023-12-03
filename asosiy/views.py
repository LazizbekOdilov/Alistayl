from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.db.models import Avg

class HomeLoginsizView(View):
    def get(self, request):
        return render(request, "page-index-2.html")


class HomeView(View):
    def get(self, request):
        content = {
            'bolimlar': Bolim.objects.all()[:8]
        }
        return render(request, "page-index.html", content)


class BolimlarView(View):
    def get(self, request):
        content = {
            'bolimlar': Bolim.objects.all()
        }
        return render(request, "page-category.html", content)

class MahsulotlarView(View):
    def get(self, request, pk):
        content = {
            'mahsulotlar': Mahsulot.objects.filter(bolim__id=pk)
        }
        return render(request, "page-listing-grid.html", content)

class MaahsulotView(View):
    def get(self, request, pk):
        izohlar = Izoh.objects.filter(mahsulot__id=pk)
        ortachasi = izohlar.aggregate(Avg("baho")).get("baho__avg")*20
        if ortachasi:
            ortachasi *= 20
        else:
            ortachasi = 0
        content = {
            'mashulot': Mahsulot.objects.get(id=pk),
            'ortachasi': ortachasi
        }
        return render(request, "page-detail-product.html", content)
    def post(self, request):
        Izoh.objects.create(
            profil = request.user,
            mahsulot = request.user,
            matn = request.POST.get("matn"),
            baho = request.POST.get("baho"),
            sana = request.POST.get("sana")
        )
        return redirect("/asosiy/mahsulot/")
