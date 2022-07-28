data = {
    'hitam': {
        'warna': 'hitam',
        'harga': 12,
    },
    'putih': {
        'warna': 'putih',
        'harga': 10,
    },
    'merah': {
        'warna': 'merah',
        'harga': 12,
    }
}

def menu():
    print(f"{'='*10}")
    print('menu')
    print(f"{'='*10}")
    print('1. Cat Hitam\n2. Cat Putih\n3. Cat Merah\n4. Exit')
    tanya = input('Mau beli apa: ')
    return tanya


while True:
    beli = menu()
    if beli == 'exit':
        break
    barang = data[beli]
    tanya = int(input('Berapa banyak: '))
    print(f"Cat{barang} sebanyak: {tanya} liter\nharga= Rp. {barang['harga']*tanya}.000")