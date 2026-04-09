#Dmytro Stefko WCY23KY3S1
#schemat z wielomianem interpolacyjnym Lagrange'a

#funkcja generujaca cienie 
def g_cienie(M, k, n, p=None):  
    F = GF(p)  #cialo 
    M_F = F(M)  #tajemnica w ciele F
    P = PolynomialRing(F, 'x')  #pierscien wielomianow
    x = P.gen()  #zmienna x
    w = [F.random_element() for _ in range(k-1)]  #losowe wspolczynniki
    f = M_F  #wyraz wolny to tajemnica
    for i, a in enumerate(w):
        f += a * x**(i+1)  #dodawanie kolejnych poteg x
    cienie = []
    for i in range(1, n+1):
        x_i = i  #numer punktu
        l_i = f(x_i)  #wartosc wielomianu
        cienie.append((x_i, l_i))  #zapisujemy pare (x, l)
    return cienie, p, f  #zwracamy liste cieni, liczbe pierwsza i wielomian

# funkcja odtwarzajaca tajemnice z cieni
def open_tajemnice(cienie, k, p):
    wybrane_cienie = cienie[:k]  #bierzemy pierwsze k cieni
    F = GF(p)  #cialo 
    M = F(0)  #wynikowy element
    for j, (x_j, y_j) in enumerate(wybrane_cienie):
        w = F(1)  #wspolczynnik Lagrange'a
        for m, (x_m, _) in enumerate(wybrane_cienie):
            if m != j:
                l = F(0 - x_m)  #licznik
                m = F(x_j - x_m)  #mianownik
                w *= l / m  #aktualizacja wspolczynnika
        M += y_j * w  #dodajemy czesc do wyniku
    return M  #zwracamy odtworzona tajemnice

#sekwencje wywolan funkcji realizujacych kroki protokolu:
M = 25 #tajemnica
k = 4   #minimalna liczba udzialow do odtworzenia
n = 5   #liczba wszystkich uczestnikow
p =71   #liczba pierwsza wieksza niz M

#krok 1 - wybor liczby pierwszej p
print("\nKrok 1")
print("liczba pierwsza wieksza niz M: p =", p)
print("minimalna liczba udzialow do odtworzenia: k =", k)
print("liczba wszystkich uczestnikow: n =", n)
print("tajemnica: M =", M)
#Po uruchomieniu programu:Krok 1
#liczba pierwsza wieksza niz M: p = 71
#minimalna liczba udzialow do odtworzenia: k = 4
#liczba wszystkich uczestnikow: n = 5
#tajemnica: M = 25 

#krok 2-4 - Generacja wielomianu i cieni
print("\nKrok 2-4")
cienie, p, f = g_cienie(M, k, n, p)
print("Wygenerowany wielomian: f(x) =", f)
print("Wygenerowane cienie:", cienie)
#Po uruchomieniu programu: Wygenerowany wielomian: f(x) = 33*x^3 + 67*x^2 + 12*x + 25
#Wygenerowane cienie: [(1, 66), (2, 13), (3, 64), (4, 62), (5, 63)]

#krok 5 - odtwarzanie tajemnicy
print("\nKrok 5")
print(k, "uczestnikow zbiera sie razem, aby odtworzyc tajemnice.")
print("Zebrane cienie:", cienie[:k])
tajemnica = open_tajemnice(cienie[:k], k, p)
print("\nOdtwarzanie tajemnicy:")
print("Odtworzona tajemnica: M =", tajemnica)
if tajemnica == M:
    print("Nice, nice! Tajemnica zostala poprawnie odtworzona.")
else:
    print("Blad! Odtworzona tajemnica rozni sie od oryginalnej.")
#Po uruchomieniu programu:4 uczestnikow zbiera sie razem, aby odtworzyc tajemnice.
#Zebrane cienie: [(1, 66), (2, 13), (3, 64), (4, 62)]

#Odtwarzanie tajemnicy:
#Odtworzona tajemnica: M = 25
#Nice, nice! Tajemnica zostala poprawnie odtworzona. 
#____________________________________________________________
#Output:
#Krok 1
#liczba pierwsza wieksza niz M: p = 71
#minimalna liczba udzialow do odtworzenia: k = 4
#liczba wszystkich uczestnikow: n = 5
#tajemnica: M = 25

#Krok 2-4
#Wygenerowany wielomian: f(x) = 39*x^3 + 48*x^2 + 10*x + 25
#Wygenerowane cienie: [(1, 51), (2, 52), (3, 49), (4, 63), (5, 44)]

#Krok 5
#4 uczestnikow zbiera sie razem, aby odtworzyc tajemnice.
#Zebrane cienie: [(1, 51), (2, 52), (3, 49), (4, 63)]

#Odtwarzanie tajemnicy:
#Odtworzona tajemnica: M = 25
#Nice, nice! Tajemnica zostala poprawnie odtworzona.