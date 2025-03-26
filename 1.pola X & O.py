# Masukkan jumlah baris dan kolom dari pengguna
jumlah_baris = int(input("Masukkan jumlah baris: "))
jumlah_kolom = int(input("Masukkan jumlah kolom: "))

# Buat pola X dan O
for baris in range(jumlah_baris):
    for kolom in range(jumlah_kolom):
        # Cek apakah jumlah indeks baris dan kolom genap
        if (baris + kolom) % 2 == 0:
            print("{:<3}".format("X"), end="") # Cetak "X" dengan lebar 3 karakter
        else:
            print("{:<3}".format("O"), end="") # Cetak "O" dengan lebar 3 karakter
    # Pindah baris setelah selesai satu baris
    print()