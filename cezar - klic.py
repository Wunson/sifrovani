#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:48:24 2017

@author: wun35247
"""

def cezar(klic,i):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ" 
    i = i%(len(klic) -1)
    posun = abeceda.index(klic[i])
    return abeceda[posun:] + abeceda[:posun]
     
        
def sifra(text,klic):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    i = 0
    for znak in text:
        abeceda2 = cezar(klic,i)
        i +=1
        if znak in abeceda:
            j = abeceda.index(znak)
            print(abeceda2[j],end = "")
        else:print(znak,end = "")
        
def desifra(text,klic):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    i = 0
    for znak in text:
        abeceda2 = cezar(klic,i)
        i +=1
        if znak in abeceda:
            j = abeceda2.index(znak)
            print(abeceda[j],end = "")
        else:print(znak,end = "")

      
######################################################
        
print("""Šifrovací program!
- mužeš psát slova odělené mazerami
- bez diakritiky
- klíčové slovo mohou velká písmena bez diakritiky
- klíčové slovo musí mít více než jeden znak""")

text = input("Sem napiš text: ").upper()
klic = input("Jaké je klíčové slovo: ").upper()

mode = input("Chceš text šifrovat/dešifrovat: ")

if "de" in mode:desifra(text,klic)
else:sifra(text,klic)

print()