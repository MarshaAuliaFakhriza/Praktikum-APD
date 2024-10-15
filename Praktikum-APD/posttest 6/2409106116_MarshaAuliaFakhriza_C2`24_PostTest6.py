akun_pengguna = {}
data_pulsa = {}

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
        if Username in akun_pengguna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi ")
        else:
            Password = input("Password: ")
            role = input("Masukkan peran (penjual/pengguna): ").lower()
            if role not in ['penjual', 'pengguna']:
                print("Peran tidak valid. Harus 'penjual' atau 'pengguna'.")
                continue
            akun_pengguna[Username] = {
                'password': Password,
                'role': role,
                'pembelian': []
            }
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username} ")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        if Username in akun_pengguna and akun_pengguna[Username]['password'] == Password:
            akun = akun_pengguna[Username]
            while True:
                print(f"\nSelamat datang {Username}!")
                print("―――Silakan pilih langkah yang kamu mau !―――")
                if akun['role'] == 'penjual': 
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
                    if akun['role'] == 'penjual':
                        jenis_pulsa = input("Jenis pulsa (contoh: Telkomsel, XL, Indosat): ")
                        harga_pulsa = input("Harga pulsa: ")
                        kuota_pulsa = input("Kuota pulsa (GB): ")
                        data_pulsa[jenis_pulsa] = {
                            'harga': harga_pulsa,
                            'kuota': kuota_pulsa
                        }
                        print("Data pulsa berhasil ditambahkan!\n")
                    else: 
                        jenis_pulsa = input("Jenis pulsa (contoh: Telkomsel, XL, Indosat): ")
                        if jenis_pulsa in data_pulsa:
                            pulsa_info = data_pulsa[jenis_pulsa]
                            akun['pembelian'].append({
                                'jenis': jenis_pulsa,
                                'harga': pulsa_info['harga'],
                                'kuota': pulsa_info['kuota']
                            })
                            print("Pulsa berhasil dibeli!\n")
                        else:
                            print("Pulsa tidak tersedia.\n")

                elif status == "2":
                    if akun['role'] == 'penjual':
                        if not data_pulsa:
                            print("Opps, saat ini kamu belum punya data pulsa, silahkan tambah data pulsa terlebih dahulu.\n")
                        else:
                            for jenis, pulsa in data_pulsa.items():
                                print(f"Jenis pulsa: {jenis}\nHarga pulsa: {pulsa['harga']}\nKuota pulsa: {pulsa['kuota']} GB\n")
                    else:
                        if not akun['pembelian']:
                            print("Opps, saat ini kamu belum punya pulsa, silahkan beli pulsa terlebih dahulu.\n")
                        else:
                            for pulsa in akun['pembelian']:
                                print(f"Jenis pulsa: {pulsa['jenis']}\nHarga pulsa: {pulsa['harga']}\nKuota pulsa: {pulsa['kuota']} GB\n")

                elif status == "3" and akun['role'] == 'penjual':
                    if not data_pulsa:
                        print("Tidak ada data pulsa yang bisa diedit.")
                    else:
                        jenis_pulsa = input("Masukkan jenis pulsa yang ingin diedit: ")
                        if jenis_pulsa in data_pulsa:
                            harga_baru = input("Masukkan harga yang baru: ")
                            kuota_baru = input("Masukkan kuota yang baru (GB): ")
                            print("Apa kamu yakin ingin mengedit data pulsa ?")
                            print("1. Iya")
                            print("2. Tidak")
                            memastikan_edit = input("Pilih: ")
                            if memastikan_edit == "1":
                                data_pulsa[jenis_pulsa] = {
                                    'harga': harga_baru,
                                    'kuota': kuota_baru
                                }
                                print("Data pulsa yang kamu pilih sudah di edit ya!\n")
                            else:
                                print("Aksi untuk mengedit data pulsa dibatalkan")

                        else:
                            print("Pulsa tidak ditemukan.\n")

                elif status == "4" and akun['role'] == 'penjual':
                    if not data_pulsa:
                        print("Tidak ada data pulsa yang bisa dihapus.")
                    else:
                        jenis_pulsa = input("Masukkan jenis pulsa yang ingin dihapus: ")
                        if jenis_pulsa in data_pulsa:
                            print("Apa kamu yakin ingin menghapus data pulsa ?")
                            print("1. Iya")
                            print("2. Tidak")
                            memastikan_hapus = input("Pilih: ")
                            if memastikan_hapus == "1":
                                del data_pulsa[jenis_pulsa]
                                print("Data pulsa yang kamu pilih sudah dihapus!\n")
                            else:
                                print("Aksi untuk menghapus data pulsa dibatalkan")
                        else:
                            print("Pulsa tidak ditemukan.\n")

                elif status == "5":
                    print("Aplikasi List Pembelian Pulsa ditutup.\n")
                    break

                else:
                    print("Input tidak valid, silahkan pilih opsi yang sesuai.\n")
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