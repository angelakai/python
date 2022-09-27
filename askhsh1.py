def gargamel(a,b):
    # Arxikopoioume to smurf se False wste na to allaksoume molis broume smurf arithmo kai na to xrhsimopoihsoume se sunthhkh sthn epanalhpsh
    smurf=False
    # Arxikopoioume to i me ton arithmo a wste na mhn ton xasoume kathws allazei mesa sthn epanalhpsh
    i=a
    # Dhmiourgoume mia epanalhpsh wste na elegksoume olous tous arithmous sto diasthma [a,b] mexri na broume enan smurf arithmo
    while i <= b and smurf==False:
        # Briskoume to plhthos pshfiwn kathe arithmou
        x=[int(j) for j in str(i)]
        # Ekxwroume th timh 0 sth metablhth sum gia na baloume to athroisma kathe arithmou
        sum=0
        # Dhmiourgoume mia epanalhpsh ksekinontas apo to 0 mexri ton arithmo twn pshfiwn kathe arithmou 
        for z in range(0,len(x)):
            # Elegxoume an o arithmos einai smurf arithmos
            num=x[z]**(z+1)
            sum +=num
        # Allazoume thn timh ths metablhths smurf se True an broume arithmo smurf wste na teleiwsei h epanalhpsh
        if i==sum:
            smurf=True
        # Auksanoume th timh ths metablhths i kata 1 gia na elegksoume ton epomeno arithmo sto diasthma
        i +=1
    return smurf

