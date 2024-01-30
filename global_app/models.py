from django.db import models

class ModelJenjangKelas(models.Model):
    id_jenjang_kelas = models.AutoField(primary_key=True)
    jenjang_kelas = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ModelGuru(models.Model):
    id_guru = models.AutoField(primary_key=True)
    nip = models.CharField(max_length=255)
    nama_guru = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ModelSiswa(models.Model):
    id_siswa = models.AutoField(primary_key=True)
    nisn = models.CharField(max_length=255)
    nama_siswa = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ModelKelas(models.Model):
    id_kelas = models.AutoField(primary_key=True)
    kode_kelas = models.CharField(max_length=255)
    nama_kelas = models.CharField(max_length=255)
    waktu = models.DateTimeField(auto_now=True)
    guru = models.ForeignKey(ModelGuru, on_delete=models.CASCADE)
    jenjang_kelas = models.ForeignKey(ModelJenjangKelas, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ModelAbsensi(models.Model):
    id_absensi = models.AutoField(primary_key=True)
    kelas = models.ForeignKey(ModelKelas, on_delete=models.CASCADE)
    siswa = models.ForeignKey(ModelSiswa, on_delete=models.CASCADE)
    tanggal_buka = models.DateTimeField()
    tanggal_tutup = models.DateTimeField()
    encrypted_text = models.CharField(max_length=255,null=True, blank=True)
    key = models.CharField(max_length=255,null=True, blank=True)
    is_attend = models.BooleanField(default=False)
    guru = models.ForeignKey(ModelGuru, on_delete=models.CASCADE)
    gambar_qr = models.ImageField(upload_to='staticfiles/qr_codes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 