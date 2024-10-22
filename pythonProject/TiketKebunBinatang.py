total=0

while True:
    umur=int(input("Masukan umur anda (Tekan -1 untuk keluar): "))
    if umur==-1:
        break

    if umur<0:
        print("Umur tidak valid")
    elif 2>=umur>=0:
        print("Gratis")
    elif 12>=umur>=3:
        print("Harga:$14")
        total+=14
    elif umur>=65:
        print("Harga:$18")
        total+=18
    elif 65>umur>=13:
        print("Harga:$28")
        total+=28
    print(f'Total:${total:.2f}')

print("______________PEMBAYARAN______________")
print(f'Total akhir:${total:.2f}')

while True:
    uang=float(input("Uang:$ "))
    if uang<0:
        print("Uang tidak valid")
    elif uang<total:
        print("Uang kurang")
    else:
        kembalian=uang-total
        print(f'Kembalian:${kembalian:.2f}')
        break






