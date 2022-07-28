def menu():
    print("==========>Makanan<==========")
    print("1.Nasi Goreng                Harga: Rp.13.000.00")
    print("2.Nasi Goreng Ati Ampela     Harga: RP.17.000.00")
    print("3.Nasi Goreng Special        Harga: Rp.20.000.00")
    print("4.Mie Goreng                 Harga: Rp.13.000.00")
    print("5.Mie Goreng Ati Ampela      Harga: Rp.15.000.00")

while True:
    menu()
    a =input("masukan pesanan: ")
    harga = 0
    if a == '1':
        porsi = int(input('berapa porsi brodi: '))
        harga = porsi * 13000
        print(f"pesanan Nasi Goreng: {porsi}\nharga: Rp.{harga}.000")
    elif a == '2':
        porsi = int(input('berapa porsi brodi: '))
        harga = porsi * 17000
        print(f"pesanan Nasi Goreng Ati Ampela: {porsi}\nharga: Rp.{harga}.000")
    elif a == "3":
        porsi = int(input('berapa porsi brodi: '))
        harga = porsi * 20000
        print(f"pesanan Nasi Goreng Special: {porsi}\nharga: Rp.{harga}.000")
    elif a == "4":
        porsi = int(input('berapa porsi brodi: '))
        harga = porsi * 13000
        print(f"pesanan Mie Goreng: {porsi}\nharga: Rp.{harga}.000")
    elif a == "5":
        porsi = int(input('berapa porsi brodi: '))
        harga = porsi * 15000
        print(f"pesanan Nasi Goreng: {porsi}\nharga: Rp.{harga}.000")
    else:
        print("masukan pesanan dengan benar!!")
    tanya = input('mau pesan lagi?? (ya/tidak) ')
    if tanya == 'tidak':
        break
