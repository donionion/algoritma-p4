hari_total = int(input("Masukkan jumlah hari: "))

tahun = int(hari_total / 365)
sisa_hari = hari_total - (tahun * 365)

bulan = int(sisa_hari / 30)
hari = sisa_hari - (bulan * 30)

print("Tahun:", tahun)
print("Bulan:", bulan)
print("Hari:", hari)