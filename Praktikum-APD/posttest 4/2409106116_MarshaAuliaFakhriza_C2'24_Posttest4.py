nama = "marsha"
password = 116
hitung = 0

while hitung < 3:
    inputnama = input("Masukkan username anda: ")
    inputpw = input("Masukkan password anda: ")
    if inputnama == nama and inputpw == password:
        print("Anda berhasil login")
        break
    else:
        print("Anda salah memasukkan username atau password")
        hitung += 1

if hitung < 3:
    while True:
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
        
        print("Program telah berakhir tentukan pilihan anda")
        print("1. Untuk mengulang program / 2. Untuk memberhentikan program")
        pilihan = int(input("Masukkan pilihan anda (1/2): "))
        if pilihan == 1:
            pass
        elif pilihan == 2:
            break
