#soal no 1
kendaraan =["motor","supra x",125,"hitam",2]
kendaraan.append("17.000.000")
kendaraan.append("GiGi")
kendaraan.insert(2,"honda")
print(kendaraan)

#soal no 2
print('''selamat datang,silahkan masukan pilihan
1.menghitung luas persegi
2.menghitung luas lingkaran
3.menghitung luas segitiga
''')
pilihan = int(input('masukan pilihan'))

match pilihan:
    case 1:
        print('1 untuk menghitung luas persegi')
        sisi = int(input('masukan sisi persegi'))
        lpersegi = sisi * sisi
        print('luas persegi dengan sisi',sisi,'yaitu',lpersegi)
    case 2:
        print('2 untuk menghitung luas lingkaran')
        r = float(input('menghitung jari-jari lingkaran'))
        llingkaran = 3.14 * r * r
        print('luas lingkaran dengan jari-jari',r,'yaitu',llingkaran)
    case 3:
        print('3 untuk menghitung luas segitiga')
        alas = int(input('masukan alas segitiga'))
        tinggi = int(input('masukan tinggi segitiga'))
        lsegitiga = 1/2 * alas * tinggi
        print('luas segitiga yaitu',lsegitiga)
    case 4:
        print('salah memilih pilihan')