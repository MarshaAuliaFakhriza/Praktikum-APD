HargaSetiapMobil = int(input("masukkan harga mobil: "))
jenisMobil = input("masukkan merk mobil (tesla, toyota, atau hyundai): ")

if jenisMobil == "tesla":
    diskon = (HargaSetiapMobil * 17) / 100
elif jenisMobil == "toyota":
    diskon = (HargaSetiapMobil * 21) / 100
elif jenisMobil == "hyundai":
    diskon = (HargaSetiapMobil * 23) / 100
else:
    print("bu Navira tidak jadi membeli mobil")
if jenisMobil in ["tesla", "toyota", "hyundai"]:
    HargaSetelahDiskon = HargaSetiapMobil - diskon
    print("harga setelah diskon:", HargaSetelahDiskon)