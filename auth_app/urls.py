
from django.urls import path
from auth_app.views import *
urlpatterns = [
    path('',login,name='login'),
    path('login-guru',loginguru,name='login-guru'),
    path('daftar',daftar,name='daftar'),
    path('daftar-guru',daftarguru,name='daftar-guru'),
    path('berhasil',berhasil,name='berhasil'),
    path('admin-area',login_admin,name='admin-area'),
]
