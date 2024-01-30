from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from guru_app.functions import *

# Create your views here.
def dashboard_guru(request):
    return render(request,'dashboard-guru.html')
def kelas_guru(request):
    return render(request,'daftar-kelas.html')
def siswa_guru(request):
    return render(request,'daftar-siswa.html')
def absensi(request):
    return render(request,'absensi.html')

@csrf_exempt
def create_qrcode(request):
    if request.method == 'POST':
        data = request.POST  # Ganti dengan request.POST jika data dikirim sebagai form data
        text = data.get('nama')
        key = data.get('key')
        print(text)
        print(key)
    
        qrcode_filename = "encrypted_qrcode2"

        create_vigenere_qrcode(text, key, qrcode_filename)
         # Berikan path ke file gambar yang baru saja dibuat
        image_path = f"qr-output/{qrcode_filename}.png"

        # Kirimkan path sebagai konteks ke template
        context = {'image_path': image_path}
        return render(request, 'hasil-generate.html', context)
    else:
        return JsonResponse({"error": "Metode tidak diizinkan"}, status=405)
    
