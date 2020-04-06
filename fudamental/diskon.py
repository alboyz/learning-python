harga = int(input("Harga Produk "))
qty = int(input("Masukan Jumlah belanja: "))
diskon = 0
if qty > 120:
    diskon = 0.15
elif qty > 100:
    diskon = 0.1
else:
    print("Tidak ada diskon")
hargaAwal = harga*qty
hargaDiskon = hargaAwal-(hargaAwal*diskon)
print("Harga Awal", hargaAwal)
print("diskon yang diberikan", int(diskon*100))
print("jumlah diskon", int(hargaAwal*diskon))
print("Harga setelah diskon", int(hargaDiskon))
