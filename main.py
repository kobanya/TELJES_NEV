'''
Teljes név   NB  2023 03 20

Készíts egy Python programot 1-teljes_nev.py néven, amely bekéri a Vezetéknevet és a Keresztnevet egy-egy változóba, majd összefűzi egy teljes_nev nevű változóba, amelyet ki kell íratni %s változójelölő segítségével!
Segítség:
(valtozo1 = input)
(valtozo2 = input)
(valtozo3 = valtozo1 + valtozo2)
(kiíratás %s)

Mintapélda
Adja meg a vezetéknevét: Kovács
Adja meg a keresztnevét: Dénes
Üdv, Kovács Dénes!

'''
vezetek = input('Adja meg a vezeték nevét: ').capitalize()  # egyik változó az első betűt átalakítja naggyá
kereszt = input('Adja meg a keresztnévét: ').capitalize()   # másik változó  az első betűt átalakítja naggyá

teljes_nev = vezetek + " " + kereszt  # szóköz a két változó között

print("Üdv, %s!" % teljes_nev)   # string , kifejezés