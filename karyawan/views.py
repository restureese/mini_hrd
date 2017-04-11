from django.shortcuts import render
# import function yang akan dieksekusi terlebih dahulu sebelum function yang akang digunakan diproses
from django.contrib.auth.decorators import login_required
from django.conf import settings

from karyawan.models import Karyawan

# Create your views here.

# LOGIN_URL = variabel di settings
@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	# SQL = select * from Karyawan where id=....
	karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
	return render(request, 'profil.html',{"karyawan":karyawan})
