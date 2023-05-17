stack = []

def tambah_buku(stack, data) :
    stack.append(data)
    print(f"{buku_baru} berhasil ditambahkan ke dalam tumpukan")

def hapus_buku_terakhir(stack):
    if len(stack) == 0 :
        print("Tumpukan  kosong tidak ada buku yang dapat dihapus")
    else :
        buku_terakhir = stack.pop()
        print(f"{buku_terakhir} barhasil dihapus dari tumpikan")

def menampilkan_buku_teratas(stack) :
    if len(stack) == 0 :
        print("Tumpukan kosong, tidak ada buku yang dapat ditampilkan")
    else :
        buku_teratas = stack[-1]
        print(f"Buku teratas didalam tumpukan adalah {buku_teratas}")

while True:
    print("\nTumpukan saat ini",stack)
    print("Menu")
    print("1. Tambah Buku dan Nama Penulis")
    print("2. Hapus buku terakhir")
    print("3. Tampilkan buku teratas")
    print("4. keluar")

    pilihan = input("Masukkan pilihan anda (1/2/3/4) : ")

    if pilihan == "1" :
        buku_baru = input("Masukkan nama buku yang akan di tambahkan  : ")
        penulis = input("Masukkan nama penulis buku : ")
        tambah_buku(stack,[buku_baru,penulis])
    elif pilihan == "2" :
        hapus_buku_terakhir(stack)
    elif pilihan == "3" :
        menampilkan_buku_teratas(stack)
    elif pilihan == "4" :
        print("Terimakasih telah menggunakan program ini")
        break
    else :
        print("Pilihan tidak valid silahkan masukkan pilihan yang benar")

