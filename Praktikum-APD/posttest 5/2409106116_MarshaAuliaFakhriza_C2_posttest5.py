akun_pengguna = []
data_pulsa = []
pulsa = []

while True:
    print("Halo! Selamat Datang di List Pembelian Pulsa ")
    print("Silakan pilih 'Daftar akun' jika belum punya akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("――――――――――――――――――――――――")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu ")
        Username = input("Username: ")
        akuna = False
        for akun in akun_pengguna:
            if akun[0] == Username:  
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi ")
        else:
            Password = input("Password: ")
            role = input("Masukkan peran (penjual/pengguna): ").lower()
            if role not in ['penjual', 'pengguna']:
                print("Peran tidak valid. Harus 'penjual' atau 'pengguna'.")
                continue
            akun_pengguna.append([Username, Password, role, []])  
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username} ")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akun_pengguna:
            if akun[0] == Username and akun[1] == Password:  
                while True:
                    print(f"\nSelamat datang {Username}!")
                    print("―――Silakan pilih langkah yang kamu mau !―――")
                    if akun[2] == 'penjual': 
                        print("1. Tambah data pulsa")
                        print("2. Lihat data pulsa")
                        print("3. Edit data pulsa")
                        print("4. Hapus data pulsa")
                    else:
                        print("1. Beli Pulsa") 
                        print("2. Lihat pulsa apa saja yang sudah di beli")
                    print("5. Exit")
                    print("―――――――――――――――――――――――――――――")

                    status = input("Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        if akun[2] == 'penjual':
                            jenis_pulsa = input("Jenis pulsa (contoh: Telkomsel, XL, Indosat): ")
                            harga_pulsa = input("Harga pulsa: ")
                            kuota_pulsa = input("Kuota pulsa (GB): ")
                            data_pulsa.append([jenis_pulsa, harga_pulsa, kuota_pulsa])  
                            print("Data pulsa berhasil ditambahkan!\n")
                        else: 
                            jenis_pulsa = input("Jenis pulsa (contoh: Telkomsel, XL, Indosat): ")
                            for pulsa in data_pulsa:
                                if pulsa[0] == jenis_pulsa:
                                    akun[3].append([jenis_pulsa, pulsa[1], pulsa[2]]) 
                                    print("Pulsa berhasil dibeli!\n")
                                    break
                            else:
                                print("Pulsa tidak tersedia.\n")

                    elif status == "2":
                        if akun[2] == 'penjual':
                            for pulsa in data_pulsa:
                                print(f"Jenis pulsa: {pulsa[0]}\nHarga pulsa: {pulsa[1]}\nKuota pulsa: {pulsa[2]} GB\n")
                            if not data_pulsa:
                                print("Opps, saat ini kamu belum punya data pulsa, silahkan tambah data pulsa terlebih dahulu.\n")
                        else:
                            for pulsa in akun[3]:
                                print(f"Jenis pulsa: {pulsa[0]}\nHarga pulsa: {pulsa[ 1]}\nKuota pulsa: {pulsa[2]} GB\n")
                            if not akun[3]:
                                print("Opps, saat ini kamu belum punya pulsa, silahkan beli pulsa terlebih dahulu.\n")

                    elif status == "3":
                        if akun[2] == 'penjual':
                            if not data_pulsa:
                                print("Tidak ada data pulsa yang bisa diedit.")
                            else:
                                edit = int(input("Data pulsa nomor berapa yang ingin kamu edit: ")) - 1
                                if 0 <= edit < len(data_pulsa):
                                    jenis_baru = input("Masukkan jenis yang baru: ")
                                    harga_baru = input("Masukkan harga yang baru: ")
                                    kuota_baru = input("Masukkan kuota yang baru (GB): ")
                                    print("Apa kamu yakin ingin mengedit data pulsa ?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_edit = input("Pilih: ")
                                    if memastikan_edit == "1":
                                        data_pulsa[edit] = [jenis_baru, harga_baru, kuota_baru]  
                                        print("Data pulsa yang kamu pilih sudah di edit ya!\n")
                                    elif memastikan_edit == "2":
                                        print("Aksi untuk mengedit data pulsa dibatalkan")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor data pulsa yang kamu maksud, silahkan input ulang.\n")

                    elif status == "4":
                        if akun[2] == 'penjual':
                            if not data_pulsa:
                                print("Tidak ada data pulsa yang bisa dihapus.")
                            else:
                                hapus = int(input("Data pulsa nomor berapa yang ingin dihapus: ")) - 1
                                if 0 <= hapus < len(data_pulsa):
                                    print(f"Apa kamu yakin ingin menghapus data pulsa ? ")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_hapus = input("Pilih: ")
                                    if memastikan_hapus == "1":
                                        del data_pulsa[hapus] 
                                        print("Data pulsa yang kamu pilih sudah dihapus!\n")
                                    elif memastikan_hapus == "2":
                                        print("Aksi untuk menghapus data pulsa dibatalkan")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor data pulsa yang kamu maksud, silahkan input ulang.\n")

                    elif status == "5":
                        print("Aplikasi List Pembelian Pulsa ditutup.\n")
                        break

                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break
        else:
            print("Username dan password anda salah, silahkan coba lagi\n")

    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar dari aplikasi?")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3\n")