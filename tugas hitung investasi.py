modal_awal = float(input("Masukkan modal awal investasi (M): "))
suku_bunga = float(input("Masukkan suku bunga tahunan dalam persen (r): "))
target_investasi = float(input("Masukkan target investasi yang ingin dicapai (T): "))

modal_sekarang = modal_awal
tahun = 0

while modal_sekarang < target_investasi:
    modal_sekarang += modal_sekarang * (suku_bunga/100)
    tahun += 1
    print(f"Tahun ke- {tahun}: Modal sekarang: {modal_sekarang:2f}")
          
    print(f"\nJumlah tahun yang dibutuhkan untuk mencapai target investasi: {tahun} tahun.")