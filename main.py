# Mengimpor modul yang diperlukan
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# Mendefinisikan fungsi enkripsi Vigenere
def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_index = 0

    # Iterasi melalui setiap karakter dalam teks masukan
    for char in plaintext:
        # Memeriksa apakah karakter adalah huruf abjad
        if char.isalpha():
            # Menghitung pergeseran berdasarkan karakter kunci yang sesuai
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Mengenkripsi karakter dan menambahkannya ke hasil
            encrypted_char = chr((ord(char.upper()) + shift - ord('A')) % 26 + ord('A'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            # Jika karakter bukan huruf abjad, tambahkan tanpa perubahan
            encrypted_text += char
    print(encrypted_text)
    return encrypted_text

# Mendefinisikan fungsi dekripsi Vigenere
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0

    # Iterasi melalui setiap karakter dalam teks terenkripsi
    for char in encrypted_text:
        # Memeriksa apakah karakter adalah huruf abjad
        if char.isalpha():
            # Menghitung pergeseran berdasarkan karakter kunci yang sesuai
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Mendekripsi karakter dan menambahkannya ke hasil
            decrypted_char = chr((ord(char.upper()) - shift - ord('A')) % 26 + ord('A'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            # Jika karakter bukan huruf abjad, tambahkan tanpa perubahan
            decrypted_text += char
    
    return decrypted_text

# Mendefinisikan fungsi untuk membuat QR code yang dienkripsi dengan Vigenere
def create_vigenere_qrcode(text, key, filename):
    encrypted_text = vigenere_encrypt(text, key)
    
    # Membuat objek QR code dengan parameter yang ditentukan
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Menambahkan teks terenkripsi Vigenere ke QR code
    qr.add_data(encrypted_text)
    qr.make(fit=True)
    # Membuat gambar QR code dengan modul bergaya dan sudut yang dibulatkan
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

    # Menyimpan gambar QR code sebagai file PNG
    filename_with_extension = filename + '.png'
    img.save(filename_with_extension)

    # Menampilkan pesan yang menandakan pembuatan QR code telah berhasil
    print(f"QR Code dengan teks '{text}' yang dienkripsi menggunakan sandi Vigenere dengan kunci '{key}' telah dibuat sebagai '{filename_with_extension}'.")

# Contoh penggunaan untuk membuat QR code terenkripsi
text_to_encode = "HELLO SEMUANYA PERKENALKAN NAMA SAYA AUFA"
encryption_key = "COBALAGI"
qrcode_filename = "encrypted_qrcode"

create_vigenere_qrcode(text_to_encode, encryption_key, qrcode_filename)

# Contoh penggunaan untuk mendekripsi teks terenkripsi
encrypted_text = "JSMLZ SKUWOOYL PKZMSOAWKGV PONA DAEI CIGA" #HASIL ENKRIPSI DARI HALO SEMUANYA PERKENALKAN NAMA SAYA AUFA
decryption_key = "COBALAGI" #KEY YANG SAMA
decrypted_text = vigenere_decrypt(encrypted_text, decryption_key)

# Menampilkan hasil dekripsi
print(f"Hasil dekripsi dari teks '{encrypted_text}' dengan kunci '{decryption_key}' adalah '{decrypted_text}'.")
