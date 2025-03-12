# Daftar film dan harga tiket
daftar_film = {
    "101"judul": "Skylines", "harga ": 60000},
    "102"judul": "Flow", "harga ": 74000},
    "103"judul": "Conclave", "harga": 47000},
    "104"judul": "Jumbo", "harga": 58000},
    "105"judul": "The Monkey", "harga": 63000},
    "106"judul": "Mickey 17", "harga": 52000},
    "107"judul": "Haunted", "harga": 66000},
               }

# Tampilan 1: Menampilkan daftar film
print("Daftar Film:")
print("Kode\Judul Film\harga")
for kode, film in daftar_film.items():
    print(f"{kode}\{film['judul']}\{film['harga']}")

# Tampilan 2: Memilih film dan jumlah tiket
kode_film = input("Masukkan kode filmyang ingin dibeli: ")
jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))

if kode_film in daftar_film:
    film = daftar_film[kode_film]
    harga_satuan = film["harga"]
    total_harga = harga_satuan * jumlah_tiket
    # Menghitungdiskon
    if total_harga > 250000:
        diskon = 0.35
    elif total_harga > 100000:
        diskon = 0.15
else: 
    diskon = 0

    potongan_harga = total_harga * diskon
    total_setelah_diskon = total_harga - potongan_harga

    # Tampilan 3: Menampilkan struk pembelian
    print("\Struk Pembelian")
    print("Nama     : [Nama Pembeli]")
    print(f"Judul Film     : {film['judul']}")
    print(f"Jumlah Tiket    : {jumlah_tiket}")
    print(f"Harga Satuan     : {harga_satuan}")
    print(f"Potongan Harga    : {potongan_harga}")
    print(f"Total Harga     : {total_setelah_diskon}")
else:
print("Kode film tidak valid.")
