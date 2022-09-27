def tril(lst):
    # Arxikopoioume to sum wste na baloume to athroisma twn trilizwn pou uparxoun
    sum=0
    # Arxikopoioume to j to opoio xreiazomaste stis epanalhpseis while gia tis sunthhkes pou tha elegxoume an uparxoun trilizes
    j=0
    # Dhmiourgoume mia epanalhsph h opoia ksekinaei apo to 0 kai teleiwnei sto megethos tou pinaka
    for i in range (len(lst)):
        # Dhmiourgoume mia epanalhpsh wste kathe fora stis sunthhkes na elegxei an uparxoun trilizes me 0 kai antistoixa 1
        while j<=1:
            # Pairnoume th periptwth pou ta 3 prwta stoixeia ths kathe grammhs tou pinaka einai idia
            if lst[i][0]==j and lst[i][1]==j and lst[i][2]==j:
                sum+=1
            # Pairnoume th periptwth pou ta 3 teleutaia stoixeia ths kathe grammhs tou pinaka einai idia
            if lst[i][1]==j and lst[i][2]==j and lst[i][3]==j:
                sum+=1
            # Pairnoume th periptwth pou ta 3 prwta stoixeia ths kathe sthlhs tou pinaka einai idia
            if lst[0][i]==j and lst[1][i]==j and lst[2][i]==j:
                sum+=1
            # Pairnoume th periptwth pou ta 3 teleutaia stoixeia ths kathe sthlhs tou pinaka einai idia
            if lst[1][i]==j and lst[2][i]==j and lst[3][i]==j:
                sum+=1
            # Auksanoume to j kata ena wste na elegxei arxika gia ta stoixeia tou pinaka pou einai 0 kai ustera 1
            j+=1
        # Dinoume th timh 0 sto j wste na mpainei sthn epanalhpsh while kathe fora pou auksanetai to i kai na exei th timh 0 afou teleiwsei wste na mpei kai sto while eksw apo thn epanalhpsh for
        j=0
        # Auksanoume to i kata ena wste na perasei apo ola ta stoixeia tou pinaka
        i+=1
    # Dhmiourgoume mia epanalhpsh wste kathe fora stis sunthhkes na elegxei an uparxoun trilizes me 0 kai antistoixa me 1
    while j<=1:
            # Elegxoume th periptwsh pou ta 3 prwta stoixeia ths kuria diagwniou tou pinaka einai idia
            if lst[0][0]==j and lst[1][1]==j and lst[2][2]==j:
                sum+=1
            # Elegxoume th periptwsh pou ta 3 teleutaia stoixeia ths kuria diagwniou tou pinaka einai idia
            if lst[1][1]==j and lst[2][2]==j and lst[3][3]==j:
                sum+=1
            # Elegxoume th periptwsh pou ta 3 prwta stoixeia ths deutereuousas diagwniou tou pinaka einai idia
            if lst[0][3]==j and lst[1][2]==j and lst[2][1]==j:
                sum+=1
            # Elegxoume th periptwsh pou ta 3 teleutaia stoixeia ths deutereuousas diagwniou tou pinaka einai idia
            if lst[1][2]==j and lst[2][1]==j and lst[3][0]==j:
                sum+=1
            # Elegxoume th periptwsh pou ta stoixeia ths diagwniou panw apo th kuria diagwnio tou pinaka einai idia
            if lst[0][1]==j and lst[1][2]==j and lst[2][3]==j:
                sum+=1
            # Elegxoume th periptwsh pou ta stoixeia ths diagwniou katw apo th kuria diagwnio tou pinaka einai idia
            if lst[1][0]==j and lst[2][1]==j and lst[3][2]==j:
                sum+=1
            # Elegxoume th periptwsh pou ta stoixeia ths diagwniou panw apo th deutereuousa diagwnio tou pinaka einai idia
            if lst[0][2]==j and lst[1][1]==j and lst[2][0]==j:
                sum+=1
            # Elegxoume th periptwsh pou ta stoixeia ths diagwniou katw apo th deutereuousa diagwnio tou pinaka einai idia
            if lst[1][3]==j and lst[2][2]==j and lst[3][1]==j:
                sum+=1
            # Auksanoume to j kata ena wste na elegksei gia ta stoixeia tou pinaka pou einai 0 kai ustera 1
            j+=1
    return sum




