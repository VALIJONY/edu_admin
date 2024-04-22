from django.db import models

# Create your models here.
class Uquvchilar(models.Model):
    ism=models.CharField(max_length=100)
    familiya=models.CharField(max_length=100)
    t_sana=models.DateField()
    tel_raqam=models.CharField(max_length=20)
    
    def __str__(self):
        return self.ism
    
class Uqituvchilar(models.Model):
    ism=models.CharField(max_length=100)
    familiya=models.CharField(max_length=100)
    yunalishi=models.CharField(max_length=100)
    tel_raqam=models.CharField(max_length=20)
    
    def __str__(self):
        return self.ism
    
class Kurslar(models.Model):
    kurs_nomi=models.CharField(max_length=100)
    narxi=models.DecimalField(max_digits=6, decimal_places=2)
    davomiyligi=models.CharField(max_length=100)
    
    def __str__(self):
        return self.kurs_nomi
    
class Tulovlar(models.Model):
    uquvchi_id=models.ForeignKey(Uquvchilar,on_delete=models.CASCADE)
    tulov=models.DecimalField(max_digits=6, decimal_places=2)
    kurs_id=models.ForeignKey(Kurslar,on_delete=models.CASCADE)
    vaqt=models.DateTimeField()
    
class Dars_xonalari(models.Model):
    xona_raqami=models.IntegerField()
    qavat=models.IntegerField()
    
    def __str__(self):
        return str(self.xona_raqami)
    
class guruh(models.Model):
    guruh=models.IntegerField()
    uquvchi_id=models.ForeignKey(Uquvchilar,on_delete=models.CASCADE)
    kurs_id=models.ForeignKey(Kurslar,on_delete=models.CASCADE)
    uqituvchi_id=models.ForeignKey(Uqituvchilar,on_delete=models.CASCADE)
    vaqt_start=models.TimeField()
    vaqt_end=models.TimeField()
    xona_id=models.ForeignKey( Dars_xonalari ,on_delete=models.CASCADE)
    
class kunlar(models.Model):
    nomi=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nomi
    
class guruh_kunlari(models.Model):
    guruh_id=models.ForeignKey(guruh,on_delete=models.CASCADE)
    kun_id=models.ForeignKey(kunlar,on_delete=models.CASCADE)