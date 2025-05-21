def main():
    konversi_nilai = {
        'A': 4.00,
        'A-': 3.75,
        'B+': 3.50,
        'B': 3.00,
        'B-': 2.75,
        'C+': 2.50,
        'C': 2.00,
        'D': 1.00,
        'E': 0.00
    }
    
# Validasi input jumlah mahasiswa
    while True:
        try:
            n = int(input("Masukkan jumlah mahasiswa: "))
            if n > 0:
                break
            print("Jumlah mahasiswa harus lebih dari 0.")
        except ValueError:
            print("Input harus berupa angka bulat.")
    
    data_mahasiswa = []
    
    for i in range(n):
        print(f"\nData mahasiswa ke-{i+1}:")
 # Validasi nama tidak kosong
        while True:
            nama = input("Nama mahasiswa: ").strip()
            if nama:
                break
            print("Nama tidak boleh kosong.")
        
 # Validasi input nilai huruf
        while True:
            nilai_huruf = input("Nilai huruf (A, A-, B+, B, B-, C+, C, D, E): ").upper()
            if nilai_huruf in konversi_nilai:
                break
            print("Nilai tidak valid. Masukkan nilai yang benar (A, A-, B+, B, B-, C+, C, D, E)")
        
        nilai_angka = konversi_nilai[nilai_huruf]
        data_mahasiswa.append([nama, nilai_huruf, nilai_angka])
    
    data_mahasiswa.sort(key=lambda x: x[2], reverse=True)
    
    print("\nHasil Perhitungan IP Mahasiswa (Tertinggi ke Terendah):")
    print("="*58)
    print("| {:<4} | {:<20} | {:<10} | {:<6} |".format("No", "Nama Mahasiswa", "Nilai", "IP"))
    print("="*58)
    for i, mahasiswa in enumerate(data_mahasiswa, 1):
        print("| {:<4} | {:<20} | {:<10} | {:<6.2f} |".format(i, mahasiswa[0], mahasiswa[1], mahasiswa[2]))
    print("="*58)
    print(f"Total mahasiswa: {n}")

if __name__ == "__main__":
    main()