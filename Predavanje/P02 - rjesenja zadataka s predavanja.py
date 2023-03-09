def najveciZbroj(a = [3, -2, 6, -5, 4, -13, 8, -6]):
    '''Funkcija traži najveći zbroj nekoliko uzastopnih elemenata liste.
       Ideja rješenja je da gledamo sve podliste zadane liste te da zbrajamo
       elemente tih podlista i u jednoj varijabli (najzbroj) čuvamo najveći takav zbroj,
       a u varijablama prvi i zadnji čuvamo početak i kraj podlite čiji je zbroj elemenata najveći
    '''
    najZbroj = -float('inf')
    prvi, zadnji = -1, -1
    for i in range(len(a)):
        for j in range(i, len(a)):
            ##i i j određuju podlistu, a s ove dvije for petlje generirati ćemo sve podliste
            ##sljedeća for petlja zbraja sve elemente podliste čiji su elementi od i do j
            s = 0
            for k in range(i, j + 1):
                s += a[k]
            if s > najZbroj:
                najZbroj = s
                prvi, zadnji = i, j
    return prvi, zadnji, najZbroj

def najveciZbroj2(a = [3, -2, 6, -5, 4, -13, 8, -6]):
    '''Funkcija radi isto što i funkcija najveciZbroj2 samo je ideja
       da to radi s manjom složenošću.
       Za svaki element provjeravamo koliki je najveći mogući zbroj nekoliko
       susjednih elemenata, koji obuhvaćaju i taj broj. Krećemo postupak raditi
       od prvog elementa liste. Ukoliko bi lista imala samo jedan element onda
       je najveći zbroj nekoliko uzastopnih elemenata liste upravo taj element.
       Ukoliko lista ima dva elementa i ukoliko promatramo najveći zbroj koji obuhvaća
       i drugi element. To će biti ili drugi element sam za sebe (ako je prvi element negativan)
       ili zbroj prva dva elementa (ako je prvi element pozitivan).
       Postupak nastavljamo raditi redom za sve elemente.
       U listi s[i-1] piše koliki je najveći zbroj nekoliko uzastopnih elemenata liste koji obuhvaća
       i element liste a na mjestu (i - 1). Najveći zbroj koji obuhvaća element a[i] je ili sam element
       a[i] (ako je s[i - 1] negativan) ili s[i - 1] + a[i] (ako je s[i - 1] pozitivan).
    ''' 
    s = [a[0]]
    najveci = -float('inf')
    for i in range(1, len(a)):
        if s[-1] < 0:
            s.append(a[i])
        else:
            s.append(a[i] + s[i - 1])
        if s[-1] > najveci:
            najveci = s[-1]
    return najveci

def umnozak(n):
    '''Funkcija koja množi prvih n prirodnih brojeva.
       Redom prolazimo po brojevima od 1 do n (uključujući) te
       svaki takav broj množimo s p. Važno je da je p na početku 1
       jer ako bi p bio jednak 0, umnožak bi uvijek bio 0.
    '''
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p

def uListi(a = [3, -2, 6, -5, 4, -13, 8, -6], e = -1):
    '''Funkcija provjerava nalazi li se element e u listi a.
       To radi tako da redom prolazi po listi a, a ako je odgovarajući
       element liste jednak elementu e funkcija vraća True.
       Ukoliko smo došli do kraja liste i nismo izašli iz funkcije (funkcija nije vratila True)
       znači da ne postoji element u listi i funkcija vraća False.
    '''
    for i in range(len(a)):
        if a[i] == e:
            return True
    ##Važno je uočiti da ovaj return False ne dolazi unutar else kod zadnje if naredbe.
    ##Ukolio bi postoja else i iza njega return False usporedio bi se samo prvi element
    ##liste te ako je on jednak e funkcija bi vratila True, a ako nije vratila bi False
    return False

def binarno_trazenje(a=[1, 7, 9, 15, 26, 29, 35, 50], e=16):
    '''Funkcija radi isto što i funkcija uListi jedino je ovaj puta lista
       sortirana (od manjeg elementa prema većemu) pa možemo malo "pametnije"
       prolaziti elementima. Prvo pogledamo srednji element liste. Ukoliko je to
       element kojeg tražimo gotovi smo. Ukoliko je traženi element manji od
       srednjeg elementa možemo zanemariti sve elemente desno od srednjeg elementa
       i na taj način listu prepoloviti. Lista ostaje ista, a mi samo gledamo granice (lijeva, desna)
       liste unutar koje tražimo element. Postupak nastavljamo sve dok ne nađemo element koji
       tražimo ili dok se granice ne preklope (dok lijeva ne postane veća od desne)
    '''
    lijeva = 0
    desna = len(a) - 1
    while lijeva <= desna:
        sredina = (desna + lijeva) // 2
        if a[sredina] == e:
            return True
        elif a[sredina] < e:
            lijeva = sredina + 1
        else:
            desna = sredina - 1
    return False

def fibonacci(n):
    '''Funkcija rekurzivno računa n-ti Fibonaccijev broj.
       1. Fibonaccijev broj je 1
       2. Fibonaccijev broj je 1
       svaki sljedeći Fibonaccijev broj je zbroj prethodna dva Fibonaccijeva broja.
       Primjerice 5. Fibonaccijev broj je zbroj 3. i 4. Fibonaccijevog broja. Odnosno
       n-ti Fibonaccijev broj je zbroj (n-1). i (n-2). Fibonaccijevog broja.
       Sama ova definicija je rekurzivna.
       Ova implementacija je spora jer se neki Fibonaccijev broj računa više puta. 
    '''
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci2(n):
    '''Kako bi se izbjeglo višestruko računanje nekog elementa Fibonaccijevog niza
       elemente pohranjujemo u listu. Sljedeći element liste je zbroj prethodna dva
       elementa liste. Prva dva Fibonaccijeva broja ne računamo, oni su 1.
    '''
    f = [1, 1]
    while len(f) < n:
        f.append(f[-1] + f[-2])
    return f[-1]


def parni(n=10):
    '''Iteratorsa funkcija koja vraća jedan po jedan paran broj od 2 do n.
       Neće napraviti listu svih parnih brojeva od 2 do n već će generirati jedan
       po jedan takav elemet (štedimo memoriju ako je lista jako velika)
       Ovu funkciju pozivamo koristeći iteratore:
       for e in parni(20):
           print(e)
    '''
    for i in range(2, n + 1, 2):
        yield i
    
def permutacije(a=[1, 2, 3]):
    '''Funkcij vraća sve permutacije (moguće rasporede) elemenata liste a.
       Ideja funkcije je rekurzivna: računalo ne zna generirati sve permutacije liste a,
       ali zna generirati sve permutacije liste koja ima jedan element manje nego lista a.
       Uzimati ćemo redom jedan po jedan element liste a te ga dodavati na prvo mjesto svih
       permutacija liste bez tog elementa
    '''
    if len(a) == 1:
        yield a
    else:
        ##redom izdvajamo jedan po jedan element liste a: 0., 1.,...
        for i in range(len(a)):
            ##kreiramo listu b koja je ista kao lista a, osim što nema element na i-tom mjestu
            b = a[:i] + a[i+1:]
            ##prolazimo kroz sve permutacije liste b
            for p in permutacije(b):
                ##vraćamo listu kod koje je na prvom mjestu i-ti element liste a
                ##a u nastavku neka permutacija liste a bez i-tog elementa
                yield [a[i]] + p

