nama = input("masukkan nama: ")
nim = input("masukkan NIM: ")

HargaSetiapMobil = float(input("masukkan harga setiap mobil: "))

#tesla
DiskonTesla = (HargaSetiapMobil * 0.17 )
HargaTesla = HargaSetiapMobil - DiskonTesla

#toyota
DiskonToyota = (HargaSetiapMobil * 0.21 )
HargaToyota = HargaSetiapMobil - DiskonToyota

#hyundai
DiskonHyundai = (HargaSetiapMobil * 0.23 )
HargaHyundai = HargaSetiapMobil - DiskonHyundai

modulus7 = HargaSetiapMobil % 7

print(f"mobil tesla seharga {HargaSetiapMobil} diskon 17% menjadi {HargaTesla: }, ")
print(f"mobil toyota seharga {HargaSetiapMobil} diskon 21% menjadi {HargaToyota: }, ")
print(f"mobil hyundai seharga {HargaSetiapMobil} diskon 23% menjadi {HargaHyundai: }, ")
print(f"dan HargaSetiapMobil modulus 7 adalah {modulus7}. ")


