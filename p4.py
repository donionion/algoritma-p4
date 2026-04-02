NamaKaryawan  = str (input(("Masukkan Nama Sales: ")))
GajiPokok = int (input(("Masukkan Gaji Pokok: ")))

PersenTunjangan = 0.2
PersenPajak = 0.15

tunjangan = PersenTunjangan * GajiPokok
pajak = PersenPajak * (GajiPokok+tunjangan)
GajiBersih = GajiPokok + tunjangan - pajak

print("Nama Karyawan: ", NamaKaryawan)
print("Gaji Bersih: ", GajiBersih)