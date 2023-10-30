
Kendaraan1 = ["avanza","Low MPV","Toyota","1,5"]
print (Kendaraan1)

Kendaraan1 = Kendaraan1 + ["putih","4","233"]
Kendaraan1.remove("Low MPV")
print(Kendaraan1)

pesan = """
menu:
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
pilih menu:
"""
pilihan=input(pesan)

match pilihan:
    case "1":
        print("anda memasukan angka 1 untuk menghitung luas persegi")
        sisi=int(input("masukan sisi:"))
        luas=sisi*sisi
        print("luas persegi dengan sisi",sisi,"adalah",luas)
    case "2":
        print("anda memasukan angka 2 untuk menghitung luas lingkaran")
        jari=int(input("masukan jari jari:"))
        luas=22/7 * jari * jari
        print("luas lingkaran dengan jari jari",jari,"adalah",luas)
    case "3":
        print("anda memasukan angka 3 untuk menghitung luas segitiga")
        alas=int(input("masukan alas:"))
        tinggi=int(input("masukan tinggi:"))
        luas=1/2*(alas*tinggi)
        print("luas segitiga dengan alas,tinggi",alas,tinggi,"adalah",luas)
