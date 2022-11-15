import math
import matplotlib.pyplot as plt
import numpy as np


# VNESI PODATKE:
d = 500 #razdalja med BS v metrih
pogresek = 0.01 #podan v radianih

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------     FUNKCIJE ZA IZRACUN NAPAKE in priprava podatkov  -----------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#vnesi dolzino v metrih, pogresek v radianih in alfo v stopinjah
def funkcijaIzZvezka(dolzina, pogresek, alfa):
    if (alfa > 179):
        alfa = 178
    beta = 90 - (alfa / 2.0)
    beta = math.radians(beta)
    alfa = math.radians(alfa)
    pogresekNaDva =  pow(pogresek, 2.0)
    dolzinaPolovic = d / 2.0
    if (math.cos(beta) == 0 or math.sin(alfa) == 0):
        povrsina = 10
    else:
        povrsina = (4.0 * pogresekNaDva * pow((dolzinaPolovic / math.cos(beta)),2)) / math.sin(alfa)

    povrsina = math.ceil(povrsina)
    return povrsina


def mojaFunkcija(dolzina, pogresek, alfa):
    beta = 90.0 - (alfa / 2.0)

    d = float(dolzina)
    pogresek = float(pogresek)
    beta = float(beta)

    beta = math.radians(beta) #pretvorimo stopinje v radiane
    #print(beta)

    betaminus = beta - pogresek
    betaplus = beta + pogresek
    #print(math.degrees(betaminus))
    #print(math.degrees(betaplus))

    d1 = (d * math.tan(betaplus))/2.0
    d2 = (d * math.tan(betaplus) * math.tan(betaminus))/(math.tan(betaminus) + math.tan(betaplus))
    #d2 = d2_calculator(d, beta, pogresek) #KUL

    #print("d1: " + str(d1))
    #print("d2: " + str(d2))

    d0 = d / 2.0 * math.tan(betaminus) #KUL
    d5 = d / 2.0 * math.tan(betaplus) #KUL
    d4 = (d2 / math.tan(betaminus)) - d / 2.0 #KUL?

    #print("d0: " + str(d0))
    #print("d5: " + str(d5))
    #print("d4: " + str(d4))

    a = d2 - d0
    b = d4
    c = d5 - d2

    #print("a: " + str(a))
    #print("b: " + str(b))
    #print("c: " + str(c))

    povrsina = abs(((a * b) / 2.0 + (b * c) / 2.0) * 2.0)
    povrsina = math.ceil(povrsina)
    return povrsina

maxnapaka = math.ceil(d * d * math.tan(pogresek) / 2.0)



x_alfa_moja = []
y_alfa_moja = []
x_alfa_solska = []
y_alfa_solska = []

x_oddaljenost_moja = []
y_oddaljenost_moja = []
x_oddaljenost_solska = []
y_oddaljenost_solska = []

x_alfa_istoObnocje_moja = []
y_alfa_istoObnocje_moja = []
x_alfa_istoObnocje_solska = []
y_alfa_istoObnocje_solska = []

x_oddaljenost_istoObnocje_moja = []
y_oddaljenost_istoObnocje_moja = []
x_oddaljenost_istoObnocje_solska = []
y_oddaljenost_istoObnocje_solska = []

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------    KONEC FUNKCIJ ZA IZRACUN NAPAKE in priprave podatkov  -------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#







# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------     IZRISOVANJE GRAFOV     ---------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# --------- PRIMERJAVA ŠOLSKE IN MOJE FORMULE ZA VELIKO ODDALJENOST OD BAZNIH POSTAJ (VELIKA NAPAKA) --------------#
# izračun je smiseln za kote med 0 in 10 stopinj. Da se razlike opazi pri isti skali za oba grafa, sem narisal kote med 1.8°in 4°.
def graf_primerjave_obeh_formul (d, pogresek):
    for alfa in range(18, 40):
        alfa = 0.1 * alfa
        povrsina_moja = mojaFunkcija(d, pogresek, alfa)
        povrsina_solska = funkcijaIzZvezka(d, pogresek, alfa)
        if ((maxnapaka < povrsina_moja) and (alfa > 170) ):
            povrsina_moja = maxnapaka
        if ((maxnapaka < povrsina_solska) and (alfa > 170) ):
            povrsina_solska = maxnapaka
        x_alfa_moja.append(alfa)
        y_alfa_moja.append(povrsina_moja)
        x_alfa_solska.append(alfa)
        y_alfa_solska.append(povrsina_solska)

    plt.plot(x_alfa_moja, y_alfa_moja, label = "moja formula")
    plt.plot(x_alfa_solska, y_alfa_solska, label = "solska formula")

    plt.title('PRIMERJAVA ŠOLSKE IN MOJE FORMULE')
    plt.xlabel('kot alfa [°]')
    plt.ylabel('velikost pogreska [m^2]')
    plt.legend()
    plt.show()

#Odkomentiraj to, če želiš narisati graf, parametre (potek kota alfa) lahko spreminjaš v definiciji funkcije "graf_primerjave_obeh_formul" 
#graf_primerjave_obeh_formul(d, pogresek)
# ------------------------------------------------------------------------------------------------------------------#
#
#
# Od tukaj naprej bom uporabljal mojo formulo, ker sem nanjo ponosen.
# Enaki rezultati predejo tudi z uporabo šolske formule, saj se od moje razlikuje le pri ekstremih napakah.
#
#
#
# --------- GRAF NAPAKE (POVRŠINE) V ODVISNOSTI OD VELIKOSTI OD VIDNEGA KOTA -------------- #
# Da ni razpon grafa prevelik (in se posledično ne bi videlo njegove oblike pri relativno majhnih vrsnostih), je narejen za kote med 20° in 180°.
# Pri kotih manjših od 20° je namreč napaka že zelo velika in je tolikokrat večja od napake pri kotih večjih od 20°, da se napake pri slednjih sploh ne oprazi (če rišeš graf od 0° do 180°.)
def graf_napake_ob_podanem_alfa (d, pogresek):
    for alfa in range(20, 180):
        povrsina_moja = mojaFunkcija(d, pogresek, alfa)
        if ((maxnapaka < povrsina_moja) and (alfa > 170) ):
            povrsina_moja = maxnapaka
        x_alfa_moja.append(alfa)
        y_alfa_moja.append(povrsina_moja)
        print("če je alfa: " + str(alfa) + ", potem moja povrsina pogreska znasaaa: " + str(povrsina_moja))

    plt.plot(x_alfa_moja, y_alfa_moja, label = "moja formula")

    plt.title('Graf napake (površine) v odvisnosti od vidnega kota')
    plt.xlabel('kot alfa [°]')
    plt.ylabel('velikost pogreska [m^2]')
    ay = plt.gca() #ta in naslednji korak obrneta x os, da kot alfa pada
    ay.set_xlim(ay.get_xlim()[::-1])
    plt.show()

#odkomentiraj če želiš narisati graf
#graf_napake_ob_podanem_alfa(d, pogresek)
# ------------------------------------------------------------------------------------------------------------------#


# --------- GRAF NAPAKE (POVRŠINE) V ODVISNOSTI OD ODDALJENOSTI UPORABNIKA OD ZVEZNICE MED BAZNIMA POSTAJAMA -------------- #
# kot alfa je pri 450metrih stran od zveznice med postajama, ki sta oddalenji ena od druge 500m, ravno dobrih 60°.
def graf_napaka_za_oddaljenost_od_zveznice(d, pogresek):
    for oddaljenost in range (0,450):
        #odmik = 0.1 * oddaljenost
        odmik = oddaljenost
        alfa = math.degrees(math.atan(odmik / (d / 2)))
        print(alfa)
        povrsina = mojaFunkcija(d, pogresek, alfa)
        if (maxnapaka < povrsina):
            povrsina = maxnapaka #ko je sprejemnik na daljici med baznima postajama bi bila površina izračunana z mojo funkcijo neskončna (deljenje z nič). Zato sem napako omejil na max vrednost

        x_oddaljenost_moja.append(odmik)
        y_oddaljenost_moja.append(povrsina)

    plt.plot(x_oddaljenost_moja, y_oddaljenost_moja, label = "moja formula")

    plt.title('Graf napake (površine) v odvisnosti od oddaljenosti uporabnika od zveznice med baznima postajama')
    plt.xlabel('oddaljenosti uporabnika [m]')
    plt.ylabel('velikost pogreska [m^2]')
    plt.show()
    print("maxnapaka: " + str(maxnapaka))
    
#odkomentiraj če želiš narisati graf
#graf_napaka_za_oddaljenost_od_zveznice (d, pogresek)
# ------------------------------------------------------------------------------------------------------------------#



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------   KONEC IZRISOVANJA GRAFOV     ---------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


































# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------     PREOSTANEK KODE (odlagalisce)    -----------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def template_funkcija ():
    for alfa in range(15, 100):
        alfa = 0.1 * alfa
        povrsina_moja = mojaFunkcija(d, pogresek, alfa)
        povrsina_solska = funkcijaIzZvezka(d, pogresek, alfa)
        if ((maxnapaka < povrsina_moja) and (alfa > 170) ):
            povrsina_moja = maxnapaka
        if ((maxnapaka < povrsina_solska) and (alfa > 170) ):
            povrsina_solska = maxnapaka
        x_alfa_moja.append(alfa)
        y_alfa_moja.append(povrsina_moja)
        x_alfa_solska.append(alfa)
        y_alfa_solska.append(povrsina_solska)
        print("če je alfa: " + str(alfa) + ", potem moja povrsina pogreska znasaaa: " + str(povrsina_moja))
        print("če je alfa: " + str(alfa) + ", potem solska povrsina pogreska znasaaa: " + str(povrsina_solska))

    print("//---------------------------------------------------//")
    print("tabela moja povrsina x: " + str(x_alfa_moja))
    print("  ---------------------------------------------------  ")
    print("tabela moja povrsina y: " + str(y_alfa_moja))
    print("  ---------------------------------------------------  ")
    print("tabela solska povrsina x: " + str(x_alfa_solska))
    print("  ---------------------------------------------------  ")
    print("tabela solska povrsina y: " + str(y_alfa_solska))
    print("//---------------------------------------------------//")

# plt.plot(x_alfa_moja, y_alfa_moja, label = "moja formula")
# plt.plot(x_alfa_solska, y_alfa_solska, label = "solska formula")

# plt.xlabel('kot alfa [°]')
# plt.ylabel('velikost pogreska [m^2]')
# plt.legend()
# plt.show()




