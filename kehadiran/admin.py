from django.contrib import admin
from kehadiran.models import Kehadiran

# Register your models here.

#list_display = field yang akan ditampilkan
#list_filter = harus yang mempunyai relasi dengan table lain
#search_fields = field yang berisi satu nilai
#list_per_page = batas penampilan table

class KehadiranAdmin (admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_kehadiran', 'waktu']
    list_filter = ('jenis_kehadiran',)
    search_fields = []
    list_per_page = 25

admin.site.register(Kehadiran, KehadiranAdmin)