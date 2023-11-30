from django.db import models
from userapp.models import Profil

class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(upload_to="bolimlar")

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=30)
    narx = models.PositiveSmallIntegerField()
    brend = models.CharField(max_length=30)
    chegirma = models.PositiveIntegerField(default=False)
    batafsil = models.TextField()
    kafolat = models.CharField(max_length=30)
    yetkazish = models.CharField(max_length=30)
    mavjud = models.BooleanField(default=True)
    davlat = models.CharField(max_length=15)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rasm}"

class  Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    matn = models.CharField(max_length=50)
    baho = models.PositiveSmallIntegerField(default=5)
    sana = models.DateTimeField()

    def __str__(self):
        return f"{self.profil}, {self.mahsulot}"
