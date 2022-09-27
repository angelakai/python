def latin(n):
    # Arxikopoioume th metablhth rom_num sthn opoia tha baloume ton arithmo sth latinikh tou morfh 
    rom_num=''
    # Oso o arithmos einai thetikos mporoume na ton metatrepsoume
    while n >0:
        # Oso o arithmos einai megaluteros h isos tou 1000 prosthetoume sth metablhth rom_num to 1000 se latinikh morfh kai ustera afairoume 1000 apo ton arithmo
        while n>=1000:
            rom_num+='M'
            n-=1000
        # Oso o arithmos einai megaluteros h isos tou 900 kai mikroteros tou 1000 prosthetoume sth metablhth rom_num to 900 se latinikh morfh kai ustera afairoume 900 apo ton arithmo
        while n>=900 and n<1000:
            rom_num+='CM'
            n-=900
        # Oso o arithmos einai megaluteros h isos tou 500 kai mikroteros tou 900 prosthetoume sth metablhth rom_num to 500 se latinikh morfh kai ustera afairoume 500 apo ton arithmo
        while n>=500 and n<900:
            rom_num+='D'
            n-=500
        # Oso o arithmos einai megaluteros h isos tou 400 kai mikroteros tou 500 prosthetoume sth metablhth rom_num to 400 se latinikh morfh kai ustera afairoume 400 apo ton arithmo
        while n>=400 and n<500:
            rom_num+='CD'
            n-=400
        # Oso o arithmos einai megaluteros h isos tou 100 kai mikroteros tou 400 prosthetoume sth metablhth rom_num to 100 se latinikh morfh kai ustera afairoume 100 apo ton arithmo
        while n>=100 and n<400:
            rom_num+='C'
            n-=100
        # Oso o arithmos einai megaluteros h isos tou 90 kai mikroteros tou 100 prosthetoume sth metablhth rom_num to 90 se latinikh morfh kai ustera afairoume 90 apo ton arithmo
        while n>=90 and n<100:
            rom_num+='XC'
            n-=90
        # Oso o arithmos einai megaluteros h isos tou 50 kai mikroteros tou 90 prosthetoume sth metablhth rom_num to 50 se latinikh morfh kai ustera afairoume 50 apo ton arithmo
        while n>=50 and n<90:
            rom_num+='L'
            n-=50
        # Oso o arithmos einai megaluteros h isos tou 40 kai mikroteros tou 50 prosthetoume sth metablhth rom_num to 40 se latinikh morfh kai ustera afairoume 40 apo ton arithmo
        while n>=40 and n<50:
            rom_num+='XL'
            n-=40
        # Oso o arithmos einai megaluteros h isos tou 10 kai mikroteros tou 40  prosthetoume sth metablhth rom_num to 10 se latinikh morfh kai ustera afairoume 10 apo ton arithmo
        while n>=10 and n<40:
            rom_num+='X'
            n-=10
        # Oso o arithmos einai megaluteros h isos tou 9 kai mikroteros tou 10 prosthetoume sth metablhth rom_num to 9 se latinikh morfh kai ustera afairoume 9 apo ton arithmo
        while n>=9 and n<10:
            rom_num+='IX'
            n-=9
        # Oso o arithmos einai megaluteros h isos tou 5 kai mikroteros tou 9 prosthetoume sth metablhth rom_num to 5 se latinikh morfh kai ustera afairoume 5 apo ton arithmo
        while n>=5 and n<9:
            rom_num+='V'
            n-=5
        # Oso o arithmos einai megaluteros h isos tou 4 kai mikroteros tou 5 prosthetoume sth metablhth rom_num to 4 se latinikh morfh kai ustera afairoume 4 apo ton arithmo
        while n>=4 and n<5:
            rom_num+='IV'
            n-=4
        # Oso o arithmos einai megaluteros h isos tou 1 kai mikroteros tou 4 prosthetoume sth metablhth rom_num to 1 se latinikh morfh kai ustera afairoume 1 apo ton arithmo
        while n>=1 and n<4:
            rom_num+='I'
            n-=1
    return rom_num
