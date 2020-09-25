from django.db import models

class Uang(models.Model):
    CATEGORY = (
        ('Simpanan Jangka Panjang', 'Simpanan Jangka Panjang'),
        ('Simpanan Jangka Pendek', 'Simpanan Jangka Pendek'),
    )

    simpanan = models.IntegerField(null=True)
    penggunaan = models.CharField(max_length=25, null=True, choices=CATEGORY)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	    return self.simpanan

class Pengguna(models.Model):
    Jabatan = (
        ('Kepala' , 'Kepala'),
        ('Admin' , "Admin"),
        ('Gudang' , "Gudang"),
    )

    Nama = models.CharField(max_length=50 , null=True)
    