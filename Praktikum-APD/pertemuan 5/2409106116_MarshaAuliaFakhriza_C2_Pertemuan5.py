# akuns = []

# while True:
#     print("halo selamat datang di aplikasi catatan")
#     print("silahkan pilih 'daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'login'")
#     print("1. daftar akun")
#     print("2. login")
#     print("3. exit")
#     print("_________________________")
#     opsi = input("pilih opsi: ")
#     print(" ")

#     if opsi == "1":
#         print("halo pengguna baru, ayo buat akun dulu")
#         username = input("username: ")
#         akuns = False
#         for akun in akuns:









# nama = ["ocha",116,True,["yuyun",145],3.96,[123,"aufa",False,3.66],"marsha"]
# print(nama[6])
# matkul = ["APD",
#           "APL",
#           "WEB",
#           "JARKOM",
#           "BASDAT",
#           "STRUKDAT",
#           "PTI",
#           "KALKULUS",
#           "PROBAS"
# ]

# print(matkul[-7])

# makanan = ["bakso","sate","soto","nasi goreng", "mie ayam", "ayam bakar", "kulit pakno", "takoyaki","grillbro"]
# print("sebelum: ")
# print(makanan[2:5])
# # makanan.append("nasi goreng")
# print("sesudah: ")
# makanan.clear()
# print(makanan)
# data = makanan.pop(5)
# print(makanan)
# del makanan[1]
# makanan.insert(2,"nasi goreng")
# makanan[0] = ["ayam", "bebek"]
# print(makanan)




# minuman = ["cola","sprite","fanta","gula", "es","teh pucuk",
#            "tehkotak"]
# minuman.insert(0,"jus tomat")
# del minuman[3]
# print(minuman)


makanan = [["bakso"], ["soto"], ["sate"],["ikan"],["bebek"]]

for i in makanan :
    if isinstance(i, list):
        for j in i :
            print(j, end="  ")
    else:
        print(i)

    # print(i, end=" ,")

