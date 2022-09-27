import urllib.request,string,re
def FileWiki(fl,url):
    # Anoigoume to arxeio pou dexetai ws eisodo 
    f = open(fl)
    file = f.read()
    f.close()
    # Dhmiourgoume lista pou perilambanei kathe xarakthra tou arxeiou
    # list_of_letters = file.translate({ord(c): None for c in string.whitespace})) An to " " den metraei ws xarakthras tote bgazoume ta kena apo olo to arxeio
    list_of_letters = list(file)
    # Metrame poses fores emfanizetai kathe xarakthras mesa sto arxeio
    count ={}
    for l in list_of_letters:
        # Elegxei an o xarakthras den einai sto count
        if l not in count:
            # An o xarakthras den einai sth lista count dhmiourgei ena stoixeio to opoio arxikopoiei se 0
            count[l] =0
        # An o xarakthras brisketai sth lista count tote kathe fora pou to briskei auksanei to plhthos tou kata 1
        count[l] +=1
    # Taksinomoume ta stoixeia tou count se fthinousa seira dhladh bazei tous xarakthres tou arxeiou se fthinousa seira analoga me to poses fores emfanizontai
    from collections import Counter
    x=Counter(count)
    # Briskoume tous xarakthres pou emfanizontai pio syxna kai kratame mono to string apo th lista me ta taksinomhmena stoixeia
    keys= [k for k, value in Counter(count).most_common()]
    # Kratame ta duo pio suxna stoixeia stis metablhtes chr1 kai chr2 antistoixa
    chr1=keys[0]
    chr2=keys[1]
    # Ekxwroume sth metablhth sum to 0 wste na broume poses fores emfanizetai to string chr1chr2 ston kwdika tou url
    sum=0
    # Anoigoume ton kwdika tou url pou dexetai apo th synarthsh
    for line in urllib.request.urlopen(url):
        urlc=line.decode('utf-8')
        # Dhmiourgoume lista pou perilambanei kathe xarakthra tou kwdika tou url
        # list_of_letters2 = urlc.translate({ord(c): None for c in string.whitespace})) An to " " den metraei ws xarakthras tote bgazoume ta kena apo olo ton kwdika tou url
        list_of_letters2 = list(urlc)
        # Dhmiourgoume mia epanalhpsh h opoia teleiwnei prin apo to teleutaio stoixeio ths listas me tous xarakthres tou kwdika url wste na mhn lambanei 1 parapanw stoixeio
        # Otan pame na elegksoume kathe stoixeio ths listas mazi me to epomeno stoixeio
        for i in range(len(list_of_letters2[:-1])):
            # Elegxoume an kathe xarakthras ths listas mazi me ton epomeno xarakthra einai idia me to string chr1chr2
            if list_of_letters2[i]+list_of_letters2[i+1]==chr1+chr2:
                # Briskoume to plhthos tou chr1chr2 
                sum+=1             
    return sum

