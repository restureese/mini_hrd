from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Divisi(models.Model):
	nama = models.CharField(max_length=40)
	keterangan = models.TextField(blank=True)

	def __str__(self):
		return self.nama

class Jabatan(models.Model):
	nama = models.CharField(max_length=40)
	keterangan = models.TextField(blank=True)

	def __str__(self):
		return self.nama

class Karyawan(models.Model):
	JENIS_KELAMIN_CHOICES = (
		('pria','Pria'),
		('wanita','Wanita'),
	)

	JENIS_KARYAWAN_CHOICES = (
		('magang','Magang'),
		('kontrak','Kontrak'),
		('tetap','Tetap'),
	)

	nama = models.CharField(max_length=40)
	alamat = models.TextField(blank=True)
	jenis_kelamin = models.CharField(max_length=10,choices=JENIS_KELAMIN_CHOICES)
	jenis_karyawan = models.CharField(max_length=10,choices=JENIS_KARYAWAN_CHOICES)
	no_telepon = models.CharField(max_length=13,blank=True)
	email = models.CharField(max_length=40,blank=True)
	pemilik_rekening = models.CharField(max_length=40)
	divisi = models.ForeignKey(Divisi)
	jabatan = models.ForeignKey(Jabatan)

	def __str__(self):
		return self.nama

class Akun(models.Model):
	JENIS_AKUN_CHOICES = (
		('karyawan','Karyawan'),
		('admin','Administrator'),
	)

	akun = models.ForeignKey(User)
	karyawan = models.ForeignKey(Karyawan)
	jenis_akun = models.CharField(max_length=20,choices=JENIS_AKUN_CHOICES)

	def __str__(self):
		return self.karyawan.nama