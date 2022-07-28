print("Kalkulator sederhana")
print("1.Penjumlahan")
print("2.pengurangan")
print("3.pembagian")
print("4.perkalian")
print("5.keluar")

while True:
    pilihan =input("masukan pilihan anda: ")
    if pilihan == "1":
        print("penjumlahan")
    elif pilihan == "2":
        print("pengurangan")
    elif pilihan == "3":
        print("pembagian")
    elif pilihan == "4":
        print("perkalian")
    elif pilihan == "5":
        break
    else:
        print("pilihan yang anda masukan salah!")


    angka1= int(input("masukan angka pertama: "))
    angka2= int(input("masykan angka kedua: "))
    if pilihan == "1":
        hasil = angka1 + angka2
        print("hasil nya adalah", hasil)
    elif pilihan == "2":
        hasil = angka1 - angka2
        print("hasil nya adalah", hasil)
    elif pilihan == "3":
        hasil = angka1 / angka2
        print("hasil nya adalah", hasil)
    elif pilihan == "4":
        hasil = angka1 * angka2
        print("hasil nya adalah", hasil)
    else:
        print("masukan angka yang benar")

        


        
