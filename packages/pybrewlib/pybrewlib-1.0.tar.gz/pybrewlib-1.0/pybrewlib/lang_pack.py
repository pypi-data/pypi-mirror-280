#!/usr/bin/env python3

"""
    language options for the library, easly extendible 
    to add new language the dictionaries need to be extended
    to change the languge lang needs to be adjusted.
"""

# "Dzisiaj nie smakowało mu nic prócz wódki samej, 
# która była – jak zawsze – niezawodna i przewidywalna. 
# Niczego nie obiecywała prócz chwilowego raju upojenia
# i długiego piekła kaca. Stawiała sprawę jasno:
# wystawię ci jutro rachunek tak wysoki,
# jak wielkie będzie twoje szczęście dzisiaj."
# ~ Marek Krajewski - Erynie
lang = "EN"
# lang pack
ALK_STR = {"EN":"Alcohol strength", "PL":"Moc alkoholu"}
WTR_QNT = {"EN":"Water quantity", "PL":"Ilosc wody"}
ALC_QNT = {"EN":"Alcohol quantity", "PL":"Ilosc alkoholu"}
OG_STR  = {"EN":"Original gravity", "PL": "OG"}
FG_STR  = {"EN":"Final gravity", "PL": "FG"}
IN_ADD  = {"EN":"Additions", "PL":"Dodan"}
GRV_B4  = {"EN":"Gravity before", "PL":"Gravity przed"}
GRV_AF  = {"EN":"Gravity before", "PL":"Gravity po"}
OPTS    = {"EN":"Options", "PL":"Opcje"}
DIL_OP  = {"EN":"Dilution calculator", "PL":"Moc rozcieczona"}
MKSG_OP = {"EN":"Build starting gravity", "PL":"Oblicz sg"}
ABV_OP  = {"EN":"Calculate ABV", "PL":"Oblicz ABV"}
DILPROP = {"EN":"Calculate dillution proportions", 
           "PL":"Oblicz proporcje rozcieczania"}
DIL_OUT = {"EN":"Dillution outcome", "PL":"Ilosc po rozcieczeniu"}
TOT_QNT = {"EN":"Total quantity", "PL":"Ilosc calosciowa"}
WNT_STR = {"EN":"Wanted strength", "PL":"Moc oczekiwana"}
NO_DRNK = {"EN":"Number of drinks", "PL":"Ilosc napojow"}
ESMXABV = {"EN":"Estimate coctail abv", "PL":"Oblicz moc drinka"}
OPT_STR = f"""{OPTS[lang]}:\n1){DIL_OP[lang]}\n2){MKSG_OP[lang]}
3){ABV_OP[lang]}\n4){DILPROP[lang]}\n5){DIL_OUT[lang]}
6){ESMXABV[lang]}\n"""