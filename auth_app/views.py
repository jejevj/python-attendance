from django.shortcuts import render,redirect
from global_app.models import *
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def login(request):
    return render(request,'login.html')
def daftar(request):
    if request.method == 'POST':
        nisn = request.POST.get('nisn')
        password = request.POST.get('password')
        nama_siswa = request.POST.get('nama_siswa')
        tempat_lahir = request.POST.get('tempat_lahir')
        tanggal_lahir = request.POST.get('tanggal_lahir')

        # Simpan data ke dalam database
        siswa = ModelSiswa(nisn=nisn, password=password, nama_siswa=nama_siswa,
                            tempat_lahir=tempat_lahir, tanggal_lahir=tanggal_lahir)
        siswa.save()

        return redirect('berhasil')
    return render(request,'daftar.html')

def loginguru(request):
    return render(request,'loginguru.html')

def daftarguru(request):
    return render(request,'daftarguru.html')

#Berhasil daftar
def berhasil(request):
    return render(request,'berhasil.html')

#ADMIN LOGIN
def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('admin_dashboard')  # Ganti 'admin_dashboard' dengan URL halaman admin yang diinginkan
        else:
            # Invalid credentials, show error message
            error_message = "Invalid username or password."
            return render(request, 'login-admin.html', {'error_message': error_message})

    return render(request, 'login-admin.html')