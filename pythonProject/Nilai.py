bobot=0
rata_rata=0

while True:
    nilai=str(input('Masukan nilai: '))
    nilai=nilai.upper()
    if nilai=='A':
        print('A=4,00')
        bobot+=4.00
        rata_rata+=1
    elif nilai=='A-':
        print('A-=3,75')
        bobot+=3.75
        rata_rata+=1
    elif nilai=='B+':
        print('B+=3,50')
        bobot+=3.50
        rata_rata+=1
    elif nilai=='B':
        print('B=3,50')
        bobot+=3.50
        rata_rata+=1
    elif nilai == 'B-':
        print('B-=2,75')
        bobot+=2.75
        rata_rata+=1
    elif nilai == 'C+':
        print('C+=2,50')
        bobot+=2.50
        rata_rata+=1
    elif nilai == 'C':
        print('C=2,00')
        bobot+=2.00
        rata_rata+=1
    elif nilai == 'C-':
        print('C-=1,75')
        bobot+=1.75
        rata_rata+=1
    elif nilai == 'D':
        print('D = 1,50')
        bobot+=1.50
        rata_rata+=1
    elif nilai == 'E':
        print('E = 1,25')
        bobot+=1.25
        rata_rata+=1
    elif nilai == '':
        print(bobot/rata_rata)
        break
    else:
        print('Nilai tidak valid')