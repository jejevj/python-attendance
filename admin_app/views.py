from django.shortcuts import render,redirect
from global_app.models import *
# Create your views here.
def admin_dashboard(request):
    return render(request, 'index-admin.html')

def manajemen_siswa(request):
    siswa_list = ModelSiswa.objects.all()
    context = {
        'siswa_list': siswa_list,
    }
    return render(request,'manajemen-siswa.html',context)

def toggle_verifikasi(request, siswa_id):
    siswa = ModelSiswa.objects.get(pk=siswa_id)

    # Toggle nilai is_verified
    siswa.is_verified = not siswa.is_verified
    siswa.save()

    return redirect('admin_siswa')

def delete_siswa(request, siswa_id):
    siswa = ModelSiswa.objects.get(pk=siswa_id)
    siswa.delete()

    return redirect('admin_siswa')


def manajemen_guru(request):
    guru_list = ModelGuru.objects.all()
    context = {
        'guru_list': guru_list,
    }
    return render(request,'manajemen-guru.html',context)

def toggle_verifikasi_guru(request, guru_id):
    guru = ModelGuru.objects.get(pk=guru_id)

    # Toggle nilai is_verified
    guru.is_verified = not guru.is_verified
    guru.save()

    return redirect('admin_guru')

def delete_guru(request, guru_id):
    guru = ModelGuru.objects.get(pk=guru_id)
    guru.delete()

    return redirect('admin_guru')