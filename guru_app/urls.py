from django.urls import path
from guru_app.views import *

urlpatterns = [
    path('dashboard',dashboard_guru,name='dashboard-guru'),
    path('kelas',kelas_guru,name='kelas-guru'),
    path('siswa',siswa_guru,name='siswa-guru'),
    path('absensi',absensi,name='absensi'),
    path('create_qrcode/', create_qrcode, name='create_qrcode'),
]
