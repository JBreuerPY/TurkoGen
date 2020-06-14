"""
Dieses Modul umfasst das Lexikon
Es enthält Datenstrukturen, die von dem Modul transducers.py importiert werden:
- Listen unregelmäßiger Verben
- Alphabetlisten
- Funktion: AnalyzeLetter
- Liste unmöglicher Kombinationen von Features
- Dicitonary, das alle Suffixe enthält
"""

from rules import APrules, MPrules


################################################################################################################################
" Lexikon unregelmäßiger Verbstämme "
################################################################################################################################

# Liste der unregelmäßigen Verbstämme
# unregelmäßige t-Assimilation
irregularStems = ["git","et","tat"]
# Die unreglemäßigen Stämme ye und de
yede = ["ye", "de"]
# Aorist: unregelmäßige Verbstämme, die einen VH1-Vokal anfügen
aoristExceptions = ["bil","gel","ver","gör","öl","al","kal","san","var","bul","dur","ol","vur"]

################################################################################################################################
" Alphabet "
################################################################################################################################

# Orthographisches Alphabet der türkischen Sprache
# Dictionary mit den Unterkategien:
# Konsonanten : {stimmhaft, stimmlos}
# Vokale : {vorne, hinten}
turkishAlphabet = {
"consonants" : {
    "voiced" : list("bcdgğjlmnrvyz"),
    "unvoiced" : list("çfhkpsşt")
},
"vowels" : {
    "back" : list("aıou"),
    "front" : list("eiöü")
}}

# Diese Funktion analysiert ein eingegebenes Symbol
# Wenn das Symbol ein Buchstabe des Türkischen Alphabets ist, wird eine Tupel zurückgegeben
# mit 0: vowel/consonant und 1: voiced/unvoiced oder back/front
# Andernfalls wird None Zurückgegeben
def analyzeLetter(letter):
    if letter in turkishAlphabet["consonants"]["voiced"]:
        letterType = "consonant"
        quality = "voiced"
    elif letter in turkishAlphabet["consonants"]["unvoiced"]:
        letterType = "consonant"
        quality = "unvoiced"
    elif letter in turkishAlphabet["vowels"]["front"]:
        letterType = "vowel"
        quality = "front"
    elif letter in turkishAlphabet["vowels"]["back"]:
        letterType = "vowel"
        quality = "back"
    else:
        return None
        
    return letterType, quality

# Alphabet der Oberflächensymbole
S = set(" ")
for letterType in turkishAlphabet:
    for quality in turkishAlphabet[letterType]:
        for List in turkishAlphabet[letterType][quality]:
            for letter in List:
                S.add(letter)
# Alphabet der Archiphoneme
A = set(APrules)
# Alphabet der Morphophoneme
M = set(MPrules)

################################################################################################################################
" Liste aller unmöglichen Kombinationen von Features "
################################################################################################################################

impossibleCombinations = [("DI","INFER"),("COND","CONDfeature"),("CONDfeature","OPT"),("NEC","CONDfeature","INFER"),("NEG","IMPOT"),("IMP","1"),("IMP","INT"),("IMP","INFER"),("IMP","CONDfeature"),("IMP","PAST")]

################################################################################################################################
" Listen aller Features "
################################################################################################################################
# Verbbasen
bases = ['PRES', 'MEKTE', 'FUTURE', 'AOR', 'MIS', 'NEC', 'DI', 'COND', 'OPT', 'IMP', "INF", "toBE"]
# Basisfeatures
baseFeatures = ['PAST', 'CONDfeature', 'INFER']
# Features
features = ['REFL', 'RECIP', 'CAUS', 'PASS', 'NEG', 'POT', 'IMPOT', 'INT', 'PART', 'PERS', 'NUM']
# Alle möglichen Features in einer Liste
allFeatures = bases+baseFeatures+features

################################################################################################################################
" Suffixe "
"""
Alle Suffixe, die das Lexikon enthält sind als Value in einem Dictionary gespeichert, die dem entsprechendem 
Feature zugeordnet sind.
"""
################################################################################################################################

suffixes = {
## Tempus- und Modusbasen
# dI-Vergangenheit
"DI" : "DI-",
# dI-Vergangenheit (Partizip)
"DIpart" : "DIK-",
# baseFeature PAST
"PAST" : "?DI-",
# Inferentiell (Basis)
"MIS" : "mIş-",
# Inferentiell (baseFeature)
"INFER" : "?mIş-",
# Futur
"FUTURE" : "YEcEK-",
# Präsens
"PRES" : "<Iyor-",
# Präsenspartizip
"PRESpart": "YEn-",
# Progressiv (Konstruktion mit mEktE)
"MEKTE" : "mEktE-",
# Aorist
"AOR" : "R-",
# Konditional (Basis)
"COND" : "sE-",
# Konditional (baseFeature)
"CONDfeature" : "!sE-",
# Notwendigkeit
"NEC" : "mElI-",
# Optativ
"OPT" : "YE-",  
# Imperativ
"IMP" : "@-",
# das Verb "sein"
"toBE" : "@-",

## Verbstammerweiterungen
# Passiv
"PASS" : "L-",
# Kausativ
"CAUS" : "C-",
# Reflexif
"REFL" : "N-",
# Repetitiv
"REPET" : "ŞtIr-",
# Reziprok
"RECIP" : "Ş-",
# Negativ
"NEG" : "M-",
# Möglichkeit
"POT" : "YEbil-",
# Unmöglichkeit
"IMPOT" : "YEM-",
## Fragepartikel
"INT" : "#mI-",
# Infinitiv
"INF" : "mEk-",

## Dictionary mit den vier Typen von Personalendungen und den Aoristendungen
# Personalendungen Typ 1
"TYPE1_1SG" : "1-",
"TYPE1_2SG":"sIn-",
"TYPE1_3SG":"@-",
"TYPE1_1PL":"YIz-",
"TYPE1_2PL":"sInIz-",
"TYPE1_3PL":"lEr-",
    
# Personalendungen Typ 2
"TYPE2_1SG":"m-",
"TYPE2_2SG":"n-",
"TYPE2_3SG":"@-",
"TYPE2_1PL":"k-",
"TYPE2_2PL":"nIz-",
"TYPE2_3PL":"lEr-",
    
# Personalendungen Typ 3
"TYPE3_1SG":"YIm-",
"TYPE3_2SG":"sIn-",
"TYPE3_3SG":"@-",
"TYPE3_1PL":"lIm-",
"TYPE3_2PL":"sInIz-",
"TYPE3_3PL":"lEr-",
    
# Personalendungen Typ 4
"TYPE4_2SG":"@-",
"TYPE4_3SG":"sIn-",
"TYPE4_2PL":"YIn-",
"TYPE4_3PL":"sInlEr-"

}