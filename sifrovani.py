# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:43:27 2017
@author: Ondra
"""
         
def sifra(klic,znak,i,abeceda):         # vypocita novy index podle klice a kodovaci abecedy
    i = i % len(klic)                   # zaručuje že index klíče nepřekročí jeho délku
    pismeno = klic[i]
    if pismeno.isdigit():
        return (abeceda.index(znak) + int(pismeno))%len(abeceda)
    else:
        return (abeceda.index(znak) + abeceda.index(klic[i]))%len(abeceda)  #přičte index kódovaného znaku a index klíčového znaku = index zašifrovaného znaku


def desifra(klic,znak,i,abeceda):       # vypocita novy index podle klice a kodovaci abecedy
    i = i % len(klic)                   # zaručuje že index klíče nepřekročí jeho délku
    pismeno = klic[i]
    if pismeno.isdigit():
        return abs((abeceda.index(znak) - int(pismeno))%len(abeceda))
    else:
        return abs((abeceda.index(znak) - abeceda.index(klic[i]))%len(abeceda))  #odečtečte index kódovaného znaku a index klíčového znaku = index dešifrovaného znaku


def cezar(text,klic):                       # po písmenech prochází text, šifruje je, a ukladda do text2
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"   # základní kodovaci abeceda
    
    mode = input("Chceš text šifrovat/dešifrovat: ")    
    if mode == "1234":                                  # při zadání kódu lze změtit kodovaci abecedu
        print("nyní je pořadí abecedy: ",abeceda)
        abeceda = input("Nové pořadí kódovací abecedy: ").upper()
        mode = input("Chceš text šifrovat/dešifrovat: ")
    text2 = ""
    i = 0
    for znak in text:
        if znak in abeceda:             # ošetřeni znaků mimo kodovací abecedu
            i += 1
            if "de" in mode:            # šifrování znaků
               text2 += abeceda[desifra(klic,znak,i,abeceda)]     
            else:
                text2 += abeceda[sifra(klic,znak,i,abeceda)]
        else:
            text2 += znak.upper()
    return text2


def main():
    print("""Šifrovací program!
- mužeš psát slova odělené mazerami
- bez diakritiky
- klíčové slovo mohou velká písmena bez diakritiky a čísla""")    
    
    text = input("Sem napiš text: ").upper()
    klic = input("Jaké je klíčové slovo: ").upper()
    
    text2 = cezar(text,klic)
    print(text2)

main()