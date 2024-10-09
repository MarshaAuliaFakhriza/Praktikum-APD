#contoh 1
# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# # contoh 2
# daftar_buku = {}

# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"

# print(daftar_buku)



# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         "Email" : "iniemail@gmail.com"
#     }
# }

# print(Biodata["KRS"][0])
# print(Biodata["Social Media"]["Eamil"])

# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legends",
#     "Game3" : "COC"
# }

# # games = dict(Sekiro = "Action", Pokemon = "Adventure",
# #              Valorant =  {"nama" : {123 : "informatika"}} )
# # print(games['Valorant']['nama'][123])


# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legends",
#     "Game3" : {
#         "nama" : "COC",
#         "genre" : "Strategy"
#     }
# }

# print((Games.get('Game3')).get('genre'))


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)


# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", 
#              "Rush Hour" : "comedy", 
#              "Oblivion" : "Science Fiction"})
# #Setelah Ditambah
# print(Film)

#Sebelum Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror'}
# #Setelah Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours':
# 'Thriller'}


# penggunaan del

# print(Film)
# simpan = Film.pop('Hours')
# # Film.clear()
# print(Film)
# Film["Hours"] = simpan
# print(Film)
# print("Jumlah Film = ", len(Film))

# movies = Film.copy()
# print(movies)
# print("Jumlah Film = ", len(movies))

# key = "apel", "jeruk", "mangga", "semangka"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)


# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")


# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
# for nama_1, nama in value.items():
#     print (nama_1, " : ", nama)
# print("")


Nilai = {
"Matematika" : 90,
"Fisika" : 80,
"Biologi" : 80,
"Kimia" : 70
}

#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

mapel = {
    "Matematika" : 90,
    "Fisika" : 80,
    "Biologi" : 80,
    "Kimia" : 70
}

nilai = sum(mapel.values())
print("Nilai total : ", nilai)  
rata = nilai / len(mapel)
print("Nilai rata-rata : ", rata)


nilai = {
    "matematika" : 90,
    "fisika" : 80,
    "biologi" : 80,
    "kimia" : 70
}

  