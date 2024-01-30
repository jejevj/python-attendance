from django.urls import path
from admin_app.views import *
urlpatterns = [
    path('admin-dashboard',admin_dashboard,name="admin_dashboard"),
    path('admin-siswa',manajemen_siswa,name="admin_siswa"),
    path('toggle_verifikasi/<int:siswa_id>/', toggle_verifikasi, name='toggle_verifikasi'),
    path('delete_siswa/<int:siswa_id>/', delete_siswa, name='delete_siswa'),
    #  GURU
    path('admin-guru',manajemen_guru,name="admin_guru"),
    path('toggle_verifikasi_guru/<int:guru_id>/', toggle_verifikasi_guru, name='toggle_verifikasi_guru'),
    path('delete_guru/<int:guru_id>/', delete_guru, name='delete_guru'),


]
