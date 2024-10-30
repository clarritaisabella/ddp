kendaraan = ['Honda Beat', 'Sepeda Motor', '120', 'pink', 2]
print("Kendaraan saya")
print(kendaraan)
print("==========")
#tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
kendaraan.append(20000000)
kendaraan.append("Metic")
kendaraan.extend([20000000, "Metic"])
print(kendaraan)
print("=========")
#tambahkan setelah jenis kendaraan dengan value [merk kendaraan],
kendaraan.insert(2, 'Honda')
print(kendaraan)
print("=========")

print('ini adalah program sederhana untuk menghitung luas bangun datar')
print("pilih menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3. Segitiga")
pilihMenu = int(input("Silahkan pilih menu dengan ketik angka 1-3"))


#tugas 2

match pilihMenu:
    case 1:
        print("ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukan nilai yang mau dihitung" ))
        hitung = sisi * sisi
        print(f"Luas persegi adalah : {hitung}")
    
    case 2:
        print("Luas Lingkaran = phi*r*r")
        r= int(input("Masukan angka"))
        phi=3.14
        luas= phi*r*r
        print(int(luas))

    case 3:
        print('ini adalah operasi luas segitiga ')
        alas= int(input('Masukan'))
        tinggi= int(input('Masukan tinggi:'))

        luas_segitiga= int(1/2*alas*tinggi)
        print(f'Luas segitiga = 1/2 *', alas, '*', tinggi, '=', luas_segitiga)
   
    case _:
         print("Pilihan tidak valid, selahkan pilih antara 1-3")