# Program Data Pelanggan Toko

no_pelanggan = []
nama_pelanggan = []
total_belanja = []

def tampilkan_menu():
    print("="*40)
    print(" PROGRAM DATA PELANGGAN TOKO ".center(40, "-"))
    print("="*40)
    print("1. Update Data")
    print("2. Hapus Data")
    print("3. Cetak Data")
    print("4. Keluar")
    print("="*40)

def update_data():
    try:
        print("\n[Update Data Pelanggan]")
        no = input("Masukkan No Pelanggan    : ")
        nama = input("Masukkan Nama Pelanggan  : ")
        total = float(input("Masukkan Total Belanja   : "))

        no_pelanggan.append(no)
        nama_pelanggan.append(nama)
        total_belanja.append(total)

        print("Data berhasil ditambahkan!\n")
    except:
        print("Terjadi kesalahan input. Coba lagi!\n")

def hapus_data():
    print("\n[Hapus Data Pelanggan]")
    no = input("Masukkan No Pelanggan yang ingin dihapus: ")
    if no in no_pelanggan:
        index = no_pelanggan.index(no)
        print(f"Data pelanggan {nama_pelanggan[index]} berhasil dihapus.\n")
        del no_pelanggan[index]
        del nama_pelanggan[index]
        del total_belanja[index]
    else:
        print("No Pelanggan tidak ditemukan.\n")

def cetak_data():
    print("\n[Daftar Data Pelanggan]")
    if len(no_pelanggan) == 0:
        print("Belum ada data pelanggan.\n")
        return
    print("="*40)
    print("{:<5} {:<15} {:>15}".format("No", "Nama", "Total Belanja"))
    print("="*40)
    for i in range(len(no_pelanggan)):
        print("{:<5} {:<15} Rp{:>12,.2f}".format(no_pelanggan[i], nama_pelanggan[i], total_belanja[i]))
    print("="*40 + "\n")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        update_data()
    elif pilihan == '2':
        hapus_data()
    elif pilihan == '3':
        cetak_data()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-4.\n")