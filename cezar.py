#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:48:24 2017

@author: wun35247
"""

def cezar(posun):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    return abeceda[posun:] + abeceda[:posun]     

def sifra(text,posun):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    abeceda2 = cezar(posun)
    for znak in text:
        if znak in abeceda:
            i = abeceda.index(znak)
            print(abeceda2[i],end = "")
        else:print(znak,end = "")

def desifra(text,posun):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    abeceda2 = cezar(posun)
    for znak in text:
        if znak in abeceda:
            i = abeceda2.index(znak)
            print(abeceda[i],end = "")
        else:print(znak,end = "")
      
##################################################
        
print("""Šifrovací program!
- mužeš psát slova odělené mazerami
- bez diakritiky
- posun je celé číslo""")

text = input("Sem napiš text: ").upper()
posun = int(input("Jaký je posun: "))

mode = input("Chceš text šifrovat/dešifrovat: ")

if "de" in mode:desifra(text,posun)
else:sifra(text,posun)

print()