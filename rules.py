"""
Dieses Modul enthält Regeln.
- APrules: Archphonemregeln
- MGrules: Morphophonemregeln
- surfaceRules: Oberflächenregeln
"""

# Regeln der Archiphoneme
APrules = {
    "@" : [["", ["else"]]],
    "#" : [[" ", ["else"]]],
    "!" : [["y", ["left_is_vowel"]],
          ["", ["else"]]],
    # Assimilation bei Anfügung von Suffixen
    "K": [["ğ", ["right_is_vowel","polysyllabic"]],
          ["ğ", ["right_Y","polysyllabic"]], 
          ["ğ", ["right_1","polysyllabic"]], 
          ["k", ["else"]]],
    "P": [["b", ["right_is_vowel","polysyllabic"]],
          ["b", ["right_Y","polysyllabic"]], 
          ["b", ["right_1","polysyllabic"]],
          ["p", ["else"]]],
    "Ç": [["c", ["right_is_vowel","polysyllabic"]],
          ["c", ["right_Y","polysyllabic"]], 
          ["c", ["right_1","polysyllabic"]],
          ["ç", ["else"]]],
    "T": [["d", ["right_is_vowel","polysyllabic"]],
          ["d", ["right_<"],"polysyllabic"],
          ["d", ["right_R"],"polysyllabic"],
          ["d", ["right_Y","polysyllabic"]],
          ["d", ["right_1","polysyllabic"]],
          ["d", ["right_is_vowel","t_exception"]],
          ["d", ["right_<"],"t_exception"],
          ["d", ["right_R"],"t_exception"],
          ["d", ["right_Y","t_exception"]],
          ["d", ["right_1","t_exception"]],
          ["t",["else"]]],
    # Assimilation von Suffixen
    "G": [["k", ["left_is_unvoiced"]],
          ["g", ["left_is_voiced"]]], 
    "C": [["ç", ["left_is_unvoiced"]],
          ["c", ["left_is_voiced"]]],
    "D": [["t", ["left_is_unvoiced"]], 
          ["d", ["left_is_voiced"]]],
    # Fugenelement
    "Y": [["y", ["left_is_vowel"]], 
          ["", ["left_is_consonant"]]],
    # Große Vokalharmonie
    "I": [['i', ["last_vowel_i"]],
          ['i', ["last_vowel_e"]],
          ['ı', ["last_vowel_ı"]],
          ['ı', ["last_vowel_a"]],
          ['u', ["last_vowel_u"]],
          ['u', ["last_vowel_o"]],
          ['ü', ["last_vowel_ü"]],
          ['ü', ["last_vowel_ö"]]],
    # Kleine Vokalharmonie
    "E": [['e', ["last_vowel_i"]],
          ['e', ["last_vowel_e"]],
          ['e', ["last_vowel_ü"]],
          ['e', ["last_vowel_ö"]],
          ['a', ["last_vowel_u"]],
          ['a', ["last_vowel_o"]],
          ['a', ["last_vowel_a"]],
          ['a', ["last_vowel_ı"]]],
    # Aorist (NEG+,INT+)
    "Z" : [["z", ["INT"]],
           ["", ["1SG","is_not_compoundTense"]],
           ["", ["1PL","is_not_compoundTense"]],
           ["z", ["else"]]]
}

# Regeln der Morphophoneme
MPrules = {
    # Negationspartikel
    "M" : [["#değil",["toBE"]],
           ["mE", ["AOR","NEG","POT","is_compoundTense"]],
           ["mE", ["AOR","IMPOT","POT","is_compoundTense"]],
           ["mEZ", ["AOR","NEG"]],
           ["mEZ", ["AOR","IMPOT"]],
           ["mE", ["else"]]],
    # Kausativ
    "C" : [["t",["polysyllabic", "left_is_vowel"]],
           ["t",["polysyllabic", "left_l"]],
           ["t",["polysyllabic", "left_r"]],
           ["DIr",["else"]]],
    # Passiv
    "L" : [["n", ["left_is_vowel"]],
           ["In", ["left_l"]],
           ["Il", ["else"]]],
    # Reflexiv
    "N" : [["n", ["left_is_vowel"]],
           ["In", ["left_is_consonant"]]],
    # Reziprok
    "Ş" : [["ş", ["left_is_vowel"]],
           ["Iş", ["left_is_consonant"]]],
    # Aorist
    "R" : [["r", ["left_is_vowel","POS"]],
           ["Er",["monosyllabic","not_aorist_exception","POS"]],
           ["Er",["auxiliary"]],
           ["Ir",["monosyllabic","aorist_exception","POS"]],
           ["Ir",["polysyllabic","left_is_consonant","POS"]],
           ["Ir",["POT","NEG"]],
           ["@", ["NEG"]],
           ["Ir",["POT"]],
           ["@", ["IMPOT"]]],
    # Getrennte Schreibweise für zusammengesetzte Formen (Leerzeichenmorphem)
    "?" : [["!", ["INT"]],
          ["#I", ["MIS","INFER"]],
          ["#I", ["MIS","PAST","CONDfeature"]],
          ["#I", ["MIS","INFER","CONDfeature"]],
          ["#I", ["DI","PAST","CONDfeature"]],
          ["!", ["else"]]],
    # Suffix 1P SG des Typ 1
    "1" : [["YIm", ["INT"]],
          ["YIm", ["AOR","POT"]],
          ["m", ["AOR","NEG","is_not_compoundTense"]],
          ["m", ["AOR","IMPOT","is_not_compoundTense"]],
          ["YIm", ["else"]]]
}

## Archiphonemregeln Extraregel zur Behandlung des < hinzufügen
for a in APrules:
    # Assimilation des Vokals zugunsten des Präsenssuffix <Iyor-
    APrules[a] = [["", ["right_<","vowel+"]]]+APrules[a]
# Oberflächenregeln
surfaceRules = [["e", ["vowel+","toBE","yede_exception"]],
                ["", ["right_<","vowel+"]],
                # Unregelmäßige Verben "ye" und "de"
                ["i", ["right_Y","vowel+","yede_exception"]],
                ["e", ["vowel+","yede_exception"]]]