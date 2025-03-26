import string

def validasi_password(password):
    """
    Memvalidasi password berdasarkan kriteria berikut:
    - Minimal 8 karakter
    - Mengandung minimal 1 huruf kecil
    - Mengandung minimal 1 huruf besar
    - Mengandung minimal 1 angka
    - Mengandung minimal 1 karakter khusus
    """
    panjang_valid = len(password) >= 8
    huruf_kecil_valid = any(c.islower() for c in password)
    huruf_besar_valid = any(c.isupper() for c in password)
    angka_valid = any(c.isdigit() for c in password)
    karakter_khusus_valid = any(c in string.punctuation for c in password)

    if (panjang_valid and huruf_kecil_valid and huruf_besar_valid and
            angka_valid and karakter_khusus_valid):
        return True
    else:
        return False

while True:
    password = input("Masukkan password: ")
    if validasi_password(password):
        print("\n--------------------------------------------")
        print("||  Password Valid! Akses diberikan.   ||")
        print("--------------------------------------------\n")
        break
    else:
        print("\n------------------------------------------------------------------")
        print("||  Password tidak valid. Coba lagi. Pastikan:                ||")
        print("||  - Minimal 8 karakter                                      ||")
        print("||  - Mengandung minimal 1 huruf kecil, 1 huruf besar,        ||")
        print("||    1 angka, dan 1 karakter khusus.                         ||")
        print("------------------------------------------------------------------\n")