nilaisiswa = [['DDG',90],['DDP',87],['PROGDAS',90]]

def menu() :
    print("===== TO DO NILAI SISWA =====")
    print("1.TAMBAH DATA")
    print("2.HAPUS DATA")
    print("3.RATA-RATA NILAI")
    print("4.TAMPILKAN DATA")
    print("5.URUTKAN DATA")
    print("6.SELESAI")

def tampilkandata() :
    print("\n===== NILAI SISWA ======")
    print("=" * 24)
    print("MAPEL            NILAI")
    print("=" * 24)
    for mapel, nilai in nilaisiswa :
        print(f"{mapel:<14} {nilai:>4}")
    print("=" * 24)

def tambahdata() :
    while True : 
        mapel = input("MASUKKAN MAPEL SISWA: ").upper().strip()
        if not mapel : 
            print("MAPEL SISWA TIDAK BOLEH KOSONG")
            continue
        found = False
        for data in nilaisiswa:
            if data[0] == mapel:
                found = True
                break
        if found:
            print(f"KAMU MEMILIKI 2 MAPEL '{mapel}' MASUKKAN MAPEL LAIN: ")
            continue
        break

    while True:
        try:
            nilai_int = int(input("MASUKKAN NILAI DARI 0-100: "))
            if 0 <= nilai_int <= 100:
                break
            else:
                print("ERROR: NILAI TIDAK BOLEH KURANG DARI 0 ATAU LEBIH DARI 100")
        except ValueError:
            print("ERROR: NILAI HARUS BERBENTUK ANGKA")
    nilaisiswa.append([mapel, nilai_int])
    print(f"MAPEL {mapel} DENGAN NILAI {nilai_int} BERHASIL DITAMBAHKAN")
    tampilkandata()

def hapusdata() :
    print("\n===== HAPUS DATA =====")
    if not nilaisiswa:
        print("DATA TIDAK DITEMUKAN")
        return
    tampilkandata()
    mapel_hapus = input("MASUKKAN NAMA MAPEL YANG INGIN DIHAPUS: ").upper().strip()

    for data in nilaisiswa:
        if data[0] == mapel_hapus:
            nilaisiswa.remove(data)
            print(f"MAPEL {mapel_hapus} BERHASIL DIHAPUS")
            tampilkandata()
            return
    print("MAPEL TIDAK DITEMUKAN")

def rata() :
    print("===== NILAI RATA-RATA SISWA =====")
    if not nilaisiswa:
        print("Data tidak ditemukan")
        return
    
    total_nilai = 0
    for mapel, nilai in nilaisiswa:
        total_nilai += nilai
    
    rata_rata = total_nilai / len(nilaisiswa)
    print(f"Rata-rata nilai siswa adalah: {rata_rata:.2f}")

def urutan() :
    while True:
        if not nilaisiswa:
            print("DATA TIDAK DITEMUKAN")
            return
        print("===== URUTAN DATA =====")
        print("1. URUTAN TERBESAR KE TERKECIL")
        print("2. URUTAN TERKECIL KE TERBESAR")
        print("3. URUTAN DARI A-Z")
        print("4. URUTAN DARI Z-A")
        pilihurutan = input("PILIH URUTAN 1-4: ")

        if pilihurutan == '1':
            terbesar = sorted(nilaisiswa, key=lambda x: x[1], reverse=True)
            print(terbesar)
            break
        elif pilihurutan == '2':
            terkecil = sorted(nilaisiswa, key=lambda x: x[1])
            print(terkecil)
            break   
        elif pilihurutan == '3':
            Azet = sorted(nilaisiswa)
            print(Azet)
            break   
        elif pilihurutan == '4':
            Zeta = sorted(nilaisiswa, reverse=True)
            print(Zeta)
            break   
        else:
            print("PILIHAN TIDAK VALID")
        tampilkandata()

def main () :
    while True :
        menu()
        pilihan = input("MASUKKAN INPUT 1-6: ")

        if pilihan == '1' :
            tambahdata()
        elif pilihan == '2' :
            hapusdata()
        elif pilihan == '3' :
            rata()
        elif pilihan == '4' :
            tampilkandata()
        elif pilihan == '5' :
            urutan()
        elif pilihan == '6' :
            print("===== TO DO NILAI SISWA TUTUP =====")
            break
        else :
            print("PILIHAN TIDAK VALID")

main()