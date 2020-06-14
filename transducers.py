"""
Dieses Modul enthält sieben Klassen:
1. Input
2. Morphotactics
3. Context
4. Lexicon
5. Rules
6. Output
7. VerbGenerator

Die Klassen vererben ihre Eigenschaften an die nächste. Dabei wird die oben aufgeführte Reihenfolge
eingehalten, bis auf die Klasse Context, die von keiner Klasse erbt.

Aufbau und Verwendung der Klassen und ihrer Methoden sind den Kommentaren zu entnehmen.
"""

# Importieren der benötigten Module
from lexicon import *
from rules import *
import numpy as np
import pandas as pd

"##############################################################################################"
# 1. Klasse: Input
# Diese Klasse verfügt über Methoden, die es dem Benutzer ermöglichen die gewünschten
# Features zu definieren, auf deren Grundlage entsprechende Verbformen generiert werden können.
# Eine Methode (acceptCombinations) vermeidet eine ungültige Kombination von Features.
# Eine weitere Methode zum Parsen der Features ist ebenfalls in dieser Klasse definiert.
"##############################################################################################"

class Input:    
    # Funktion, die eine Liste wiedergibt, die alle bereits definierten Features enthält
    def allFeatures(self):
        # Features, die per Default vordefiniert sind in einer Liste speichern
        features = [self.stem,self.features["NUM"],self.features["PERS"],self.base]
        # Features, die der User definieren kann, der Liste hinzufügen
        for dic in [self.baseFeatures, self.features]:
            features += [feature for feature in dic if dic[feature] == True]
        return features
    
    # Funktion zur Überprüfung der grammatischen Logik.
    # Bei ungültigen Kombinationen von Features wird ein Fehler aufgerufen und der letzte Schritt rückgängig gemacht
    def acceptCombinations(self,currentFeature):
        # Kontollvariable <accept> definieren und auf True setzen
        accept = True
        # Liste aller bereits gesetzten Features erstellen
        features = self.allFeatures()
        # Über Liste mit unmöglichen Kombinationen von Features iterieren
        for combi in impossibleCombinations:
            # Wenn unkombinierbare Features in der Featureliste enthalten sind
            if all(x in features for x in combi) == True:
                # setzte <accept> auf False
                accept = False
        # Wenn <accept> auf False gesetzt wurde
        if accept == False:
            ## das zuletzt gesetzte Feature zurücksetzen und Fehlermeldung ausgeben
            # Wenn Verbbasis falsch gesetzt wurde diese zurücksetzen, Fehlermeldung ausgeben
            if currentFeature == self.base:
                self.base = "PRES"
                raise AssertionError("Wrong combination of features. '"+currentFeature+"' was set back to default (PRES).")
            # Wenn Basisfeature oder Feature falsch gesetzt wurde dieses zurücksetzen, Fehlermeldung ausgeben
            # über die dicts der Basisfeatures und Features iterieren
            for dic in [self.baseFeatures, self.features]:
                # über jedes Feature des aktuellen dicts iterieren
                for key2 in dic:
                    # Wenn das zuletzt gesetzte Feature im aktuellen dict ist
                    if currentFeature in dic:
                        # Wenn das Feature nicht "PERS" (Person) ist
                        # (Alle Features außer "PERS" und "NUM" sind boolsche Werte)
                        if currentFeature != "PERS":
                            # Feature auf False zurücksetzten
                            dic[currentFeature] = False
                            # Fehlermeldung ausgeben
                            raise AssertionError("Wrong combination of features. '"+currentFeature+"' was set back to False.")
                        # Feature "PERS" auf Default (3) zurücksetzten
                        # Wenn das Feature "PERS" ist
                        else:
                            # Featrue "PERS" auf Default "3" zurücksetzten
                            dic[currentFeature] = "3"
                            # Fehlermeldung ausgeben
                            raise AssertionError("Wrong combination of features. '"+currentFeature+"' was set back to default (3).")
                   
    
    ############################## Alle Features mit einer Eingabeliste setzen ################################
    # Diese Methode erhält eine Liste mit Strings und setzt die darin enthaltenen Entrsprechungen der features
    # auf die entspreechenden Werte (True oder Modifikation des Strings)
    def setFeatures(self,featureList):
        # Über die Eingabeliste iterieren
        for feature in featureList:
            # Basis
            if feature in bases:
                self.base = feature
                self.acceptCombinations(feature)
            # Basisfeatures
            if feature in baseFeatures:
                self.baseFeatures[feature] = True
                self.acceptCombinations(feature)
            # Alle anderen Features deren Variablen boolesche Werte sind
            if feature in features or feature[:-1] in features:
                # Ausnahme: Kausativ
                if feature == "CAUS":
                    # Variable für Kausativvorkommen auf 1 setzen
                    self.causativeOccurrences = 1
                    self.features[feature] = True
                    self.acceptCombinations(feature)
                # Ausnahme: Kausativ mit Spezifikation, wie oft er vorkommen soll
                elif len(feature) == 5 and feature[:-1] == "CAUS":
                    # Variable für Kausativvorkommen auf entsprechende zahl setzen
                    self.causativeOccurrences = int(feature[-1])
                    self.features[feature[:-1]] = True
                    self.acceptCombinations(feature[:-1])
                # Alle anderen Features werden per Default auf True gesetzt
                else:
                    self.features[feature] = True
                    self.acceptCombinations(feature)
            # Strings für Person modifizieren
            if feature in ["1","2","3"]:
                self.features["PERS"] = feature
                self.acceptCombinations(feature)
            # Strings für Numerus modifizieren
            if feature in ["SG","PL"]:
                self.features["NUM"] = feature
                self.acceptCombinations(feature)
            
    ########################### Base (Modus- und Tempusbasen) ###########################
    
    # Funktion, mit der die Basis "base" gesetzt werden kann.
    # Die Eingabe erfordert einen String, wobei nur die Abkürzungen der Tempus- und Modusbasen akzeptiert werden:
    # ['PRES', 'MEKTE', 'FUTURE', 'AOR', 'MIS', 'NEC','DI', 'COND', 'OPT', 'IMP', "INF", "toBE"]
    def setBase(self,base="PRES"):
        if base not in bases:
            raise AssertionError('Only bases from the following List are allowed:',bases)
        else:
            self.base = base
        self.acceptCombinations(base)
        # Ausnahme für das Verb "sein"
        if self.base == "toBE":
            # Wenn letzter Buchstabe ein k,t,ç oder p ist, durch ein Archiphonem erstetzen
            self.stem = self.stem[:-1]+self.stem[-1].replace("k","K").replace("t","T").replace("ç","Ç").replace("p","P")
    
    ########################### baseFeatures (erweiternde Modus- und Tempusbasen) ###########################
    
    # Beim aufrufen der folgenden Methoden werden die entsprechenden Variablen per Default auf True gesetzt.
    # Wird ein boolscher Wert als Argument übergeben wird die Variable entsprechend verändert.
    
    # Funktion, mit der das baseFeature "past" auf True oder False gesetzt werden kann
    def setPast(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.baseFeatures["PAST"] = True
        else:
            self.baseFeatures["PAST"] = False
        self.acceptCombinations("PAST")
            
    # Funktion, mit der das baseFeature "conditional" auf True oder False gesetzt werden kann
    def setConditional(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.baseFeatures["CONDfeature"] = True
        else:
            self.baseFeatures["CONDfeature"] = False
        self.acceptCombinations("CONDfeature")
            
    # Funktion, mit der das baseFeature "inferential" auf True oder False gesetzt werden kann
    def setInferential(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.baseFeatures["INFER"] = True
        else:
            self.baseFeatures["INFER"] = False
        self.acceptCombinations("INFER")
            
    ########################### Features ###########################
    
    # Beim aufrufen der folgenden Methoden werden die entsprechenden Variablen per Default auf True gesetzt.
    # Wird ein boolscher Wert als Argument übergeben wird die Variable entsprechend verändert.
    
    # Methode, mit der das Feature "reflexive" auf True oder False gesetzt werden kann
    def setReflexive(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["REFL"] = True
        else:
            self.features["REFL"] = False
        self.acceptCombinations("REFL")

    # Methode, mit der das Feature "reciprocal" auf True oder False gesetzt werden kann
    def setReciprocal(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["RECIP"] = True
        else:
            self.features["RECIP"] = False
        self.acceptCombinations("RECIP")
            
    # Methode, mit der das Feature "causative" auf True oder False gesetzt werden kann
    def setCausative(self,value=True, occurrences=1):
        if type(value) != bool:
            raise ValueError("'value' input has to be be boolean.")
        if value == True:
            self.features["CAUS"] = True
        else:
            self.features["CAUS"] = False
        if type(occurrences) != int:
            raise ValueError("'occurrences' input has to be be integer.")
        else:
            self.causativeOccurrences = occurrences
        self.acceptCombinations("CAUS")
            
    # Methode, mit der das Feature "passive" auf True oder False gesetzt werden kann
    def setPassive(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["PASS"] = True
        else:
            self.features["PASS"] = False
        self.acceptCombinations("PASS")
            
    # Methode, mit der das Feature "negated" auf True oder False gesetzt werden kann
    def setNegated(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["NEG"] = True
        else:
            self.features["NEG"] = False
        self.acceptCombinations("NEG")
            
    # Methode, mit der das Feature "potential" auf True oder False gesetzt werden kann
    def setPotential(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["POT"] = True
        else:
            self.features["POT"] = False
        self.acceptCombinations("POT")
            
    # Methode, mit der das Feature "impotential" auf True oder False gesetzt werden kann
    def setImpotential(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["IMPOT"] = True
        else:
            self.features["IMPOT"] = False
        self.acceptCombinations("IMPOT")
            
    # Methode, mit der das Feature "interrogative" auf True oder False gesetzt werden kann
    def setInterrogative(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["INT"] = True
        else:
            self.features["INT"] = False
        self.acceptCombinations("INT")
        
    # Methode, mit der das Feature "participle" auf True oder False gesetzt werden kann
    def setParticiple(self,value=True):
        if type(value) != bool:
            raise ValueError("Input has to be be boolean.")
        if value == True:
            self.features["PART"] = True
        else:
            self.features["PART"] = False
        self.acceptCombinations("PART")
        
    ############################## Person und Numerus ##############################
            
    # Methode, mit der das Feature "person" bestimmt werden kann.
    # Erlaubte Eingaben sind die Zahlen 1-3 als String.
    # Per Default ist der Wert auf "3" gesetzt.
    def setPerson(self,person="3"):
        if person not in list("123"):
            raise ValueError("Input has to be a String (1, 2 or 3).")
        else:
            self.features["PERS"] = person
        self.acceptCombinations("PERS")
            
    # Methode, mit der das Feature "number" bestimmt werden kann.
    # Erlaubte Eingaben sind "SG" oder "PL" als String.
    # Per Default ist der Wert auf "SG" gesetzt.
    def setNumber(self,number="SG"):
        if number not in ["SG","PL"]:
            raise ValueError("Input has to be a String (SG or PL).")
        else:
            self.features["NUM"] = number
            
"##############################################################################################################"
# 2. Klasse: Morphotactics
# Diese Klasse erbt die Eigenschaften der Klasse <Input>
# Sie behandelt das Teilproblem der Morphotaktik
# Es ist eine Methode <morphotactics> enthalten
"###############################################################################################################"
class Morphotactics(Input):
    
    ############################
    "2.1 parseFeatures"
    ############################
    # Diese Methode parst die gegebenen Features. Sie gibt eine Liste der Features in zugelassener Reihenfolge wieder.
    # Anhand einer Abfolge von Anweisungen wird die zulässige Reihenfolge der Features ermittelt, welche jeweils ein Suffix repräsentieren
    # Jedes akzeptierte Feature wird in die vordefinierte Featureliste Liste eingefügt, welche nach der vollständigen
    # Abhandlung der Anweisungen ausgegeben wird.
    # Eine Beispielausgabe kann sein ['git', 'OPT', '3SG', 'INT']
    def parseFeatures(self):
        # definiere eine Liste, in der die Features in der zulässigen Reihenfolge aufgenommen werden
        # Der Verbstamm ist positionell unveränderbar und somit das erste Element der Liste
        feature_list = [self.stem]
        # Alle vorhandenen Features in korrekter Reihenfolge in die Liste einfügen
        ## Stammverändernde Features 1
        # Die Kombination mit dem verb "sein" ist unmöglich, wird daher an dieser Stelle vermieden
        if self.base != "toBE":
            # Reflexiv
            if self.features["REFL"] == True:
                feature_list.append("REFL")
            # Reziprok
            if self.features["RECIP"] == True:
                feature_list.append("RECIP")
            # Kausativ
            if self.features["CAUS"] == True:
                for i in range(self.causativeOccurrences):
                    feature_list.append("CAUS")
            # Passiv
            if self.features["PASS"] == True:
                feature_list.append("PASS")
            
        ## Stammverändernde Features 2
        # Negation ohne Potentialis
        if self.features["NEG"] == True:
            feature_list.append("NEG")
        # Die Kombination mit dem verb "sein" ist unmöglich, wird daher an dieser Stelle vermieden
        if self.base != "toBE":
            # Potentialis
            if self.features["IMPOT"] == True:
                feature_list.append("IMPOT")
            # Impotentialis
            if self.features["POT"] == True:
                feature_list.append("POT")
            
        ## Basis
        # Wenn ein Partizip definiert wurde
        if self.features["PART"] == True:
            # Präsens: Für das Suffix des Partizip Präsens existiert ein eigener Eintrag im Lexikon "PRESpart",
            # welcher der Liste hinzugefügt wird
            if self.base == "PRES":
                feature_list.append("PRESpart")
            # DI-Vergangenheit: entsprechendes Feature "DIpart" Featureliste hinzufügen
            elif self.base == "DI":
                feature_list.append("DIpart")
            # Default
            else:
                # Für alle anderen Formen wird die regelmäßige Endung der Basis verwendet, daher diese der Liste hinzufügen
                feature_list.append(self.base)
            # Featureliste wiedergeben (Das Partizip ist an dieser Stelle nicht erweiterbar)
            return feature_list
        # Basis hinzufügen
        feature_list.append(self.base)
            
        # Die Infinitivform ist weiter nicht veränderbar, somit werden keine weiteren Features berücksichtig,
        # solange "INF" als Basis gesetzt wurde.
        if self.base != "INF":
            # Fragepartikel
            if self.features["INT"] == True:
                # Ausnahmen für Personalendungen Typ 2 und 3: 
                if self.base in ["COND","DI","OPT"] or self.features["PERS"]+self.features["NUM"] == "3PL":
                    feature_list.append(self.features["PERS"]+self.features["NUM"])
                feature_list.append("INT") 

            ## baseFeatures
            # past
            if self.baseFeatures["PAST"] == True:
                feature_list.append("PAST")
            # inferential
            if self.baseFeatures["INFER"] == True:
                feature_list.append("INFER")
            # conditionalFeature
            if self.baseFeatures["CONDfeature"] == True:
                feature_list.append("CONDfeature")

            # Personalendung für Typ 1 und Typ 4
            # Person & Numerus
            if self.features["PERS"]+self.features["NUM"] not in feature_list:
                feature_list.append(self.features["PERS"]+self.features["NUM"])
        
        return feature_list
    
    
"##############################################################################################################"
# 3. Klasse: Context
# Diese Klasse verfügt über Methoden, die dazu verwendet werden, den Kontext des aktuellen
# Zustandes während einer Übergangsfunktion zu ermitteln.
# Mit der Methode <attributes> kann eine Liste erstellt werden, die den aktuellen Kontext enthält
# der Kontext wird repräsentiert, durch eine Liste von Attributen, die Informationen über die
# linken/rechten Symbole, Ausnahmen und Features enthalten.
# Folgende Attribute können hierbei übergeben werden:
# ['right_X', 'left_X', 'last_vowel_X', 'left_is_vowel', 'right_is_vowel', 'left_is_unvoiced', 'left_is_voiced', 
# 'left_is_consonant', 'is_not_compoundTense', 'is_compoundTense' ,'polysyllabic',  'monosyllabic', 
# 'auxiliary', 'yede_exception', 'not_aorist_exception', 'aorist_exception','vowel+', 'vowel-', 't_exception','not_t_exception']
# Die gesetzten Features werden ebenfalls der Liste der Attribute hinzugefügt
"###############################################################################################################"

class Context:
    # Ein Objekt dieser Klasse wird instanziiert durch vier Attribute:
    # - currentSymbol: Das aktuelle Symbol, das von seiner lexikalischen in eine Oberflächenform umgewandelt wird
    # - currentState: Der aktuelle Zustand des Transduktors (siehe Klasse Transducers -> surfaceTransition)
    # - intermediateLevel: Der lexikalische String, der rechten Seite des aktuellen Symbols
    # - features: Eine Liste aller Features, die definiert wurden
    def __init__(self, currentSymbol, currentState, intermediateLevel, features):
        # Das aktuelle zu bearbeitende Symbol
        self.symbol = currentSymbol
        # Der aktuelle Zustand (intermediate,surface)
        self.state = (currentState[0],currentState[1].replace("-","").replace("+","").replace(" ","").replace("0",""))
        # Der weiter zu bearbeitende lexikalische String
        self.intermediate = intermediateLevel.replace("-","").replace("+","").replace("@","")
        # Liste der Features
        self.features = features
        
    # Die Qualität des Letzten Vokals ist ausschlaggebend für die Regeln der Vokalharmonie
    # Diese Methode gibt das Kontextattribut <last_vowel_X> zurück, wobei X den letzten Vokal bezeichnet
    def lastVowel(self):
        vowel = ""
        # iteriere über den umgekehrten, bereits generierten Oberflächenstring
        for letter in self.state[1][::-1]:
            # Sobald ein Vokal identifiziert wurde, diesen <vowel> zuweisen
            if analyzeLetter(letter) != None and analyzeLetter(letter)[0] == "vowel":
                vowel = letter
                break
        # Ausnahme für Stämme deren letzter Vokal assimiliert wurde (Kontrollfeature: <)
        if vowel == "":
            # iteriere über den umgekehrten lexikalischen String des Stamms
            for letter in self.features[0][::-1]:
                if analyzeLetter(letter) != None and analyzeLetter(letter)[0] == "vowel":
                    vowel = letter
                    break
        # Feature in einer Liste wiedergeben
        return ["last_vowel_"+vowel]
    
    # Wenn das Feature <NEG> (negiert) nicht in der Liste der Features ist, gibt diese Methode
    # das Kontextattribut <POS> (positiv) wieder.
    def positive(self):
        if "NEG" not in self.features and "IMPOT" not in self.features:
            return ["POS"]
        else:
            return []
    
    # Diese Methode analysiert den Kontext des Stamms und gibt auskunft über unregelmäßigkeiten
    # des Aorist, der Stämme "ye" und "de" sowie der Stämme "git", "tat" und "et".
    # Bei "et" werden ebenfalls geprüft, ob es sich um eine Komposition des Hilfsverbs "etmek" handelt.
    # Es können die Kontextattribute <aorist_exception>, <not_aorist_exception>, <auxiliary>, <t_exception> und
    # <yede_exception>
    def exceptions(self):
        output = []
        # Unregelmäßige Verbstämme im Aorist
        if self.state[1] in aoristExceptions:
            output += ["aorist_exception"]
        # Regelmäßige Verbstämme im Aorist
        else:
            output += ["not_aorist_exception"]
        ### unregelmäßige Stämme mit T-Assimilation
        # T-Ausnahme
        if len(self.state[0]) >= 2 and self.state[0][-2:] in ["et","ed"] or len(self.state[0]) >= 3 and self.state[0][-3:] in ["tat","git","tad","gid"]:
            output += ["t_exception"]
        # keine T-Ausnahme
        else:
            output += ["not_t_exception"]
        # Komposition mit Hilfsverb
        if len(self.state[1]) >= 2 and self.state[1][-2:] in ["et","ed"]:
            output += ["auxiliary"]
        # Unregelmäßige Stämme ye und de
        if len(self.state[0]) >= 2 and self.state[0][-2:] in ["ye","de"]:
            output += ["yede_exception"]
        return output
        
    # Diese Methode prüft, ob es sich um eine Zusammengesetzte Form handelt
    # Es werden die Kontextattribute <is_compoundTense> oder <is_not_compoundTense> wiedergegeben.
    def compoundTense(self):
        if any(x in ["CONDfeature","INFER","PAST"] for x in self.features) == True:
            return ["is_compoundTense"]
        else:
            return ["is_not_compoundTense"]
    
    # Diese Methode prüft, ob der bisher generierte Oberflächenstring einsilbig oder mehrsilbig ist
    # Es werden die Kontextattribute <monosyllabic> oder <polysyllabic> wiedergegeben.
    def syllables(self):
        vowels = [letter for letter in self.state[1] if analyzeLetter(letter) != None and analyzeLetter(letter)[0] == "vowel"]
        if len(vowels) == 1:
            return ["monosyllabic"]
        else:
            return ["polysyllabic"]
            
    # Diese Methode gibt analyziert den linken Kontext und gibt die folgenden Kontextattribute wieder:
    # <left_X> (X=letzes Symbol des bereits generierten Oberflächenstring)
    # <left_is_X> (X= voiced|unvoiced)
    def left(self):
        output = []
        try:
            # letztes Symbol der linken Seite
            output.append("left_"+self.state[1][-1])
        except:
            pass
        try:
            info = analyzeLetter(self.state[1][-1])
            # Vokal oder Konsonant
            output.append("left_is_"+info[0])
            if info[0] == "consonant":
                output.append("left_is_"+info[1])
            else:
                output.append("left_is_voiced")
            return output
        except:
            pass
        return output
        
    # Diese Methode gibt analyziert den rechten Kontext und gibt die folgenden Kontextattribute wieder:
    # <right_is_X> (X=consonant|vowel)
    # <right_is_X> (X= voiced|unvoiced)
    # <right_X> (X=nächstes Symbol des rechten lexikalischen Strings (intermediateLevel)
    def right(self):
        try:
            output = []
            # Symbol analysieren und in <info> speichern
            info = analyzeLetter(self.intermediate[0])
            # Wenn rechtes Zeichen im Alphabet vorhanden ist
            if info != None:
                # Vokal oder Konsonant
                output.append("right_is_"+info[0])
                if info[0] == "consonant":
                    output.append("right_is_"+info[1])
                else:
                    output.append("right_is_voiced")
            # Wenn rechtes Zeichen ein Archiphonem, Morphophonem oder Feature ist
            else:
                # Das erste Symbol der rechten Seite anfügen und output hinzufügen
                output.append("right_"+self.intermediate[0])
                # Informationen über Archiphoneme und Morphophoneme ergänzen
                if self.intermediate[0] in list("IENLŞ"):
                    output.append("right_is_voiced")
                    output.append("right_is_vowel")
            # Outputliste ausgeben
            return output
        except:
            return []
        
    # Methode, die prüft, ob das aktuelle Symbol ein Vokal oder Konsonant ist
    # Es werden die Kontextattribute <vowel+> oder <consonant+> wiedergegeben.
    def current(self):
        try:
            output = []
            # aktuelles Symbol
            output.append("current_"+self.symbol)
            # Vokal
            if analyzeLetter(self.symbol) != None and analyzeLetter(self.symbol)[0] == "vowel":
                output.append("vowel+")
            elif self.symbol in list("EI:"):
                output.append("vowel+")
            # Konsonant
            elif analyzeLetter(self.symbol) != None and analyzeLetter(self.symbol)[0] == "consonant": 
                output.append("consonant+")
            elif self.symbol in list("KGTDÇCBT"):
                output.append("consonant+")
            
            return output
        except:
            return []
        
    # Diese Methode ruft alle Methoden der Klassen auf und speichert alle Kontextattribute in einer Liste
    # Diese Liste wird weiterhin durch die gesetzen Features erweitert
    def attributes(self):
        atts = self.features+self.left()+self.right()+self.syllables()+self.exceptions()+self.lastVowel()+self.current()+self.positive()+self.compoundTense()
        # Liste mit Attributen wiedergeben
        return atts
    
    
"##############################################################################################"
# 4. Klasse: Lexicon
# Diese Klasse erbt die Eigenschaften der Klasse Morphotactics.
# Sie enthält Methoden, die als Transduktor fungieren, die verwendet werden, um Features
# in lexikalische Repräsentationen von Suffixen und diese in Oberflächenrepräsentationen
# zu übersetzen.
"##############################################################################################"

class Lexicon(Morphotactics):
        
    ############################
    "4.1 lexiconFST"
    ############################
    # Diese Methode gibt ein dictionary zurück, in dem jedem Feature ein entsprechendes Suffix
    # zugeordnet ist. An dieser Stelle wird entschieden, welche Personalendung verwendet wird. Die Features
    # Person und Numerus werden mit dem entsprechenden Typ kombiniert und als ein Feature verstanden.
    # Eine Beispielausgabe kann sein: {'git': 'git+', 'OPT': 'YE-', '3SG': '@-', 'INT': '#mI-'}
    def lexiconFST(self):
        # leeres dict erstellen
        featureDict = {}
        # eine Liste der geparsten Features erstellen
        features = self.parseFeatures()
        # über <features> iterieren
        for feature in features:
            # Für ein Feature, dass nicht direkt einem Suffix zugeordnet ist
            if feature not in suffixes:
                # Verbstamm
                if feature == self.stem:
                    # Der Verbstamm hat keine spezielle Bezeichnung und bezeichnet sich im dict als sich selbst
                    # das Symbol für die Stammgrenze "+" wird dem Stamm angefügt
                    featureDict[feature] = feature+"+"
                # Wenn feature eine Personalendung beschreibt
                elif feature[0] in "123" and "CONVERB" not in features:
                    ## Entsprechende Personalendungen auswählen
                    # Typ 2
                    if features[features.index(feature)-1] in ["DI","COND","CONDfeature","PAST"]:
                        featureDict[feature] = suffixes["TYPE2_"+feature]
                    # Typ 3
                    elif features[features.index(feature)-1] == "OPT":
                        featureDict[feature] = suffixes["TYPE3_"+feature]
                    # Typ 4
                    elif features[features.index(feature)-1] == "IMP":
                        featureDict[feature] = suffixes["TYPE4_"+feature]
                    # Typ 1
                    else:
                        featureDict[feature] = suffixes["TYPE1_"+feature]
            # Wenn feature ein entsprechendes Suffix hat
            else:
                # Suffic dem Feature zuordnen
                featureDict[feature] = suffixes[feature]
        # dict ausgeben
        return featureDict
        
    "##########################################################################################################"
    # Intermediärer Transduktor
    # Der intermediäre Transduktor Überführt eine gegebene Liste von Features in einen String aus 
    # lexikalischen Symbolen, die vom lexikalischen Transduktor übergeben werden. Er besteht aus der 
    # Übergangsfunktion <intermediateTransition> und der Ausführungsfunktion <intermediateFST>
    # Die Ausgabe ist eine Tupel mit 0: Eine Liste der Features und 1: der intermediäre String.
    # Eine Beispielausgabe kann sein: (['git', 'OPT', '3SG', 'INT'], '^git+YE-@-#mI-$')
    "##########################################################################################################"
        
    ############################
    "4.2 intermediateTransition"
    ############################
    # Die Übergangsfunktion für die Oberfläche
    def intermediateTransition(self, currentFeature, currentState, features):
        # Dictionary erstellen, mit den entsprechenden lexikalischen Einträgen der Features
        morphDict = self.lexiconFST()
        # Variable für nächsten Zustand zuweisen
        nextState = currentState
        nextState[0].append(currentFeature)
        nextState[1] += morphDict[currentFeature]
        return nextState
    
    ############################
    "4.3 intermediateFST"
    ############################
    # Funktion zur Ausführung des Transduktors zum Generieren der Oberflächenebene
    def intermediateFST(self):
        # Liste der geparsten Features erstellen
        features = self.parseFeatures()
        # Aktueller Zustand
        currentState = [[],""]
        # Liste der bereits erstelten Zustände
        states = []
        # Abbruchbedingung für folgende while-Schleife, bei erreichen des Endzustandes
        finalStateReached = False
        while finalStateReached != True:
            currentFeature = features.pop(0)
            currentState = self.intermediateTransition(currentFeature, currentState, features)
            states.append((tuple(currentState[0]),currentState[1]))
            if len(features) == 0:
                finalStateReached = True
        # Startsymbol $ und Schlusssymbol € anfügen
        currentState[1] = "^"+currentState[1]+"$"
        return tuple(currentState)
    

"##########################################################################################################"
# 5. Klasse: Rules
# Diese Klasse erbt die Eigenschaften der Klasse Lexicon.
# Sie enthält zwei Methoden, zur Ausführung des Oberflächentransduktors.
# Der Oberflächentransduktor übersetzt einen intermediären String in einen Oberflächenstring.
# Er besteht aus der Übergangsfunktion <surfaceTransition> und der Ausführungsfunktion <surfaceFST>
# Die Ausgabe ist eine Liste aller Zustände, wobei ein Zustand eine Tuple ist mit 0:intermediärer String
# und 1: Oberflächenstring.
# Eine Beispielausgabe kann sein:
#[('', ''),
# ('^', ''),
# ('^g', 'g'),
# ('^gi', 'gi'),
# ('^git', 'gid'),
# ('^git+', 'gid'),
# ('^git+Y', 'gid'),
# ('^git+YE', 'gide'),
# ('^git+YE-', 'gide'),
# ('^git+YE-@', 'gide'),
# ('^git+YE-@-', 'gide'),
# ('^git+YE-@-#', 'gide '),
# ('^git+YE-@-#m', 'gide m'),
# ('^git+YE-@-#mI', 'gide mi'),
# ('^git+YE-@-#mI-', 'gide mi'),
# ('^git+YE-@-#mI-$', 'gide mi')]
"##########################################################################################################"
    
class Rules(Lexicon):
    ############################
    "5.1 surfaceTransition"
    ############################
    # Eingabe:
    # - currentSymbol: Das aktuelle lexikalische Symbol
    # - currentState: Der aktuelle Zustand, der eine Tupel ist, bestehend aus einem lexikalischen String und einem Oberflächenstring
    # - intermediateLevel: Der Noch zu bearbeitende lexikalische String
    # - features: Die Liste der morphologischen Features, die gesetzt wurden
    def surfaceTransition(self,currentSymbol, currentState, intermediateLevel, features):
        # Variable <nextState> für den nächsten Zustand definieren, zunächst mit aktuellem Zustand gleichsetzen
        nextState = currentState
        # lexikalischen String des nächsten Zustands um aktuelles lexikalisches Symbol erweitern
        nextState[0] += currentSymbol
        # Wenn der Oberflächenstring von <nextState> nicht leer ist
        if currentState[1] != "":
            # Eine Liste erstellen, mit Features, die den Kontext beschreiben
            context = Context(currentSymbol, currentState, intermediateLevel, features).attributes()
        # Wenn der Oberflächenstring von <nextState> leer ist
        else:
            # Kontext als Leere Liste definieren
            context = []
                        
        ##################### Unregelmäßige T-Assimilation #####################
        # Ausnahmeregel: <currentSymbol> das Archiphonem <T> zuweisen
        if currentSymbol == "t" and "t_exception" in context:
            currentSymbol = "T"
                
        ##################### Regeln der Morphophoneme #####################
        # Wenn aktuellem Symbol Morphophonemregeln zugewiesen sind
        if currentSymbol in MPrules:
            # Über Liste mit Morphophonemregeln iterieren
            for rule in MPrules[currentSymbol]:
                # Wenn die Regel zutrifft
                if all(attribute in context  for attribute in rule[1]) == True:
                    # ersetze <currentSymbol> mit entsprechendem Morphem
                    currentSymbol = rule[0]
                    # Nach zutreffen einer Regel Schleife abbrechen
                    break
                # Wenn die Regel "else" enthält trifft sie immer zu
                elif "else" in rule[1]:
                    currentSymbol = rule[0]
                    
        ##############################################################################################
        # -> Nach der Übersetzung der Morphophoneme kann <currentSymbol> mehr als ein Symbol enthalten 
        # -> Hier wird Übergangsfunktion Rekursiv für jedes Symbol weitergeführt                       
        #### Über jedes Element in <currentSymbol> iterieren 
        for symbol in currentSymbol:
            ### Kontext ###
            # Wenn <symbol> nicht das letzte Element aus <currentSymbol> ist
            if currentSymbol.index(symbol) != len(currentSymbol)-1:
                # Kontext aktualisieren: Den Rest des Strings <currentSymbol> mit einbeziehen
                context = Context(symbol, currentState, currentSymbol[currentSymbol.index(symbol)+1:]+intermediateLevel, features).attributes()
            # Wenn <symbol> das letzte Element ist
            else:
                # Kontext aktualisieren
                context = Context(symbol, currentState, intermediateLevel, features).attributes()
                
            ##################### Regeln der Archiphoneme #####################
            # Wenn aktuellem Symbol Archiphonemregeln zugewiesen sind
            if symbol in APrules:
                # Über Liste mit Regeln iterieren
                for rule in APrules[symbol]:
                    # Wenn die Regel zutrifft
                    if all(attribute in context  for attribute in rule[1]) == True:
                        # Oberfläche um entsprechendes Symbol der Regel erweitern
                        nextState[1] += rule[0]
                        # Nach zutreffen einer Regel Schleife abbrechen
                        break
                    # Wenn die Regel "else" enthält trifft sie immer zu
                    if "else" in rule[1]:
                        nextState[1] += rule[0]
                        
            ##################### Oberflächensymbole #####################
            # Wenn symbol ein Oberflächensymbol sein kann
            if analyzeLetter(symbol) != None:
                # Kontrollvariable <ruleUsed> auf False setzen
                ruleUsed = False
                # über <surfaceRules> iterieren
                for rule in surfaceRules:
                    # Wenn die Regel zutrifft
                    if all(attribute in context  for attribute in rule[1]) == True:
                        # erweitere die Oberfläche um das entsprechende Symbol der Regel
                        nextState[1] += rule[0]
                        # Kontrollvariable auf True setzen
                        ruleUsed = True
                        # Nach zutreffen einer Regel Schleife abbrechen
                        break
                # Nach zutreffen einer Regel aktuellen Schleifendurchlauf beenden
                if ruleUsed == True:
                    continue
                # Wenn keine Oberflächenregel zutrifft
                else:
                    # Oberfläche durch unverändertes, aktuelles Symbol erweitern
                    nextState[1] += symbol
                        
        # nächsten Zustand wiedergeben
        return nextState
    
    ############################
    "5.2 surfaceFST"
    ############################
    def surfaceFST(self):
        # lexikalischen Transduktor ausführen und variablen zuweisen
        # Features und intermdiären String speichern
        features,intermediateLevel = self.intermediateFST()
        # Aktueller Zustand
        currentState = ["",""]
        # Liste der bereits erstelten Zustände
        states = []+[tuple(currentState)]
        # Abbruchbedingung für folgende while-Schleife, bei erreichen des Endzustandes
        finalStateReached = False
        # While-Schleife: Solange kein Endzustand erreicht wurde
        while finalStateReached != True:
            ## Eingaben für die Übergangsfunktion
            # aktuelles Symbol: Erstes Symbol des lexikalischen Strings
            currentSymbol = intermediateLevel[0]
            # Erstes Symbol des lexikalischen Strings entfernen
            intermediateLevel = intermediateLevel[1:]
            # aktuellen Zustand mit Übergangsfunktion aktualisieren
            currentState = self.surfaceTransition(currentSymbol, currentState, intermediateLevel, features)
            # Neuen Zustand der Liste mit Zuständen hinzufügen
            states.append(tuple(currentState))
            # Wenn die Länge des lexikalischen Strings leer ist
            if len(intermediateLevel) == 0:
                # Abbruchbedingung auf True setzen
                finalStateReached = True
        # Liste aller Zustände wiedergeben
        return states
    
"##############################################################################################"
# 6. Klasse: Output
# Diese Klasse erbt die Eigenschaften der Klasse <Rules>
# Sie verfügt über benutzerfreundliche Methoden, mit der Verbformen anhand der Nutzereingabe 
# generiert werden können.
"##############################################################################################"

class Output(Rules):        
    ############################
    "6.2 form"
    ############################
    # Diese Methode gibt die generierte Wortform aus
    # Hierbei wird die Funktion <surfaceTransducer> aufgerufen, dessen Ausgabe eine Liste der Zustände ist.
    # Ein Zustand ist eine Tupel mit 0:Lexikalischer String und 1:Oberflächenstring
    # Die gewünschte Wortform ist also der Oberflächenstring des Endzustandes
    def form(self):
        return self.surfaceFST()[-1][-1]
    
    ############################
    "6.3 conjugate"
    ############################
    # Diese Methode gibt einen Dataframe (Pythonmodul: pandas) zurück, der ein Paradigma
    # der Konjugierten Verbform enthält
    def conjugate(self):
        # features speichern
        oldNumber = self.features["NUM"]
        oldPerson = self.features["PERS"]
        # leeres dictionary erstellen
        conjugation = {}
        # Über Numeri SG und PL iterieren
        for number in ["SG","PL"]:
            # Eintrag für Numerus in dict erstellen, falls nicht vorhanden
            if number not in conjugation:
                conjugation[number] = {}
            # Über Person 1,2,3 iterieren
            for person in ["1","2","3"]:
                # entsprechenden Numerus und Person setzen
                self.setNumber(number)
                self.setPerson(person)
                # generierte Wortform entsprechnden Numerus und Person als Wert hinzufügen
                conjugation[number][person] = self.form()
        # Mehrdimensionales Dict in einen Dataframe umwandeln
        dataFrame = pd.DataFrame(data=(conjugation))
        # ursprüngliche Features wiederherstellen
        self.setNumber(oldNumber)
        self.setPerson(oldPerson)
        # Dataframe wiedergeben
        return dataFrame
    
    ############################
    "6.4 paradigm"
    ############################
    # Diese Methode gibt ebenfalls einen Dataframe wieder, der abhängig von der Verbbasis erstellt wird.
    # Basis "toBE": Ein Paradigma der zusammengesetzten Formen in Kombination mit dem Verb "sein"
    # alle anderen Basen: Ein Paradigma der zusammengesetzten Formen in Kombination mit der entsprechenden Verbbasis
    def paradigm(self):
        # ursprüngliche Features speichern
        oldBase = self.base
        oldFeatures = self.baseFeatures
        # Features auf False setzen
        self.baseFeatures = {
            "PAST":False,
            "CONDfeature":False,
            "INFER":False
        }
        # Zeilennamen bestimmen, abhängig von der Verbbasis
        # "toBE"
        if self.base == "toBE":
            bases = ["toBE"]
        # alle anderen Basen
        else:
            bases = ["PRES","FUTURE","AOR","MIS","DI","COND","OPT","NEC"]
        # dictionary erstellen
        # Für jede Basis werden die entsprechenden Formen in Kombination mit den Basisfeatures generiert und
        # der entsprechenden Basis im dict zugeordnet
        # Bei jedem Durchlauft wird eine Ausnahmebehandlung eingesetzt, wobei bei jeder unmöglichen Kombination
        # ein leerer String als Platzhalter übergeben wird
        table = {}
        for base in bases:
            # Base
            table[base] = []
            try:
                # simple
                self.setBase(base)
                table[base] += [self.form()]
            except:
                table[base] += [""]
            try:
                # PAST
                self.setBase(base)
                self.setPast()
                table[base] += [self.form()]
            except:
                table[base] += [""]
            self.setPast(False)
            try:
                # CONDfeature
                self.setBase(base)
                self.setConditional()
                table[base] += [self.form()]
            except:
                table[base] += [""]
            self.setConditional(False)
            try:
                # PAST & CONDfeature
                self.setBase(base)
                self.setPast()
                self.setConditional()
                table[base] += [self.form()]
            except:
                table[base] += [""]
            self.setConditional(False)
            self.setPast(False)
            try:
                # INFER
                self.setBase(base)
                self.setInferential()
                table[base] += [self.form()]
            except:
                table[base] += [""]
            self.setInferential(False)
            try:
                # INFER & CONDfeature
                self.setBase(base)
                self.setInferential()
                self.setConditional()
                table[base] += [self.form()]
            except:
                table[base] += [""]
            self.setInferential(False)
            self.setConditional(False)
        
        # Einstellungen wiederherstellen
        self.baseFeatures = oldFeatures
        self.base = oldBase

        # Spalten- und Zeilennamen in Listen
        columnNames = ["Simple","Past","Conditional","Past & Conditional","Inferential","Inferential & Conditional"]
        # "toBE"
        if self.base == "toBE":
            rowNames = ["to be"]
        # Alle anderen Basen
        else:
            rowNames = ["Present","Future","Aorist","miş-past","di-past","Conditional","Optative","Necessitative"]
        
        # Spalten- und Zeilennamen einen Index zuweisen
        # Zeilen
        rowIndexes = {}
        for index in range(len(rowNames)):
            rowIndexes[index] = rowNames[index]
        # Spalten
        columnIndexes = {}
        for index in range(len(columnNames)):
            columnIndexes[index] = columnNames[index]
        
        # Dataframe erstellen
        dataFrame = pd.DataFrame(np.array([table[i] for i in table]))
        # Spalten und Zeilen umbenennen
        dataFrame.rename(columns=columnIndexes,index=rowIndexes,inplace=True)
        # Dataframe ausgeben
        return dataFrame
    
    ############################
    "6.5 analyze"
    ############################
    # Diese Methode gibt einen Dataframe wieder, der die Beziehung zwischen Suffixen und Features veranschaulicht
    # Hierfür werden die Archiphonemregeln so modifiziert, dass Morphemgrenzen in Form eines "-" auf der Oberfläche 
    # erscheinen, so dass diese seperierbar sind.
    def analyze(self):
        # Regeln modifizieren
        APrules["-"] = [["-", ["else"]]]
        APrules["+"] = [["-", ["else"]]]
        APrules["@"] = [["@", ["else"]]]
        # Liste mit seperierten Suffixen des Oberflächenlevels erstellen: Form mit Trennzeichen "-" generieren und splitten
        surfaceSuffixes = [s.replace("@","") for s in self.form().split("-") if s != ""]
        # Liste mit seperierten Suffixen des Zwischenlevels erstellen: Form generieren und an Trennzeichen splitten
        intermediateSuffixes = [s for s in self.surfaceFST()[-1][0].replace("+","-").replace("$","").replace("^","").split("-") if s != ""]
        # Sortierte Liste der Features erstellen (Lexikalischer Level)
        feat = self.parseFeatures()
        # Dataframe erstellen und Zeilen benennen
        dataFrame = pd.DataFrame(np.array([feat,intermediateSuffixes,surfaceSuffixes]))
        dataFrame.rename(index={0:"Lexical",1:"Intermediate",2:"Surface"},inplace=True)
        # Modifizierung der Regeln wieder rückgängig machen
        del APrules["-"]
        del APrules["+"]
        APrules["@"] = [["", ["else"]]]
        # Dataframe ausgeben
        return dataFrame
    
    
"##############################################################################################"
# 7. Klasse: VerbGenerator
# Diese Klasse erbt die Eigenschaften der Klasse <Output>
# Sie dient als ausführende Klasse des gesamten Generierungssystems und verfügt über
# eine Instanzierungsfunktion
"##############################################################################################"

class VerbGenerator(Output):
    ############################
    "7.1 Instanziierung"
    ############################
    def __init__(self,stem):
        # Für jedes Symbol der Eingabe prüfen, ob es ein zulässiger Buchstabe des Alphabets ist
        for letter in stem:
            if analyzeLetter(letter) == None and letter != " ":
                # Bei falscher Eingabe Fehlermeldung ausgeben
                raise AssertionError("Some characters are not in the alphabet, please check your input.")
        # Es ist möglich einen Verbstamm oder eine Infinitivform anzugeben
        # Bei einer eingegebenen Infinitivform wird die Form auf den Stamm reduziert und gespeichert
        if len(stem) >= 3 and stem[-3:] in ["mek","mak"]:
        # Es ist möglich getrennt geschriebene Hilfsverben einzugeben
        # Hierbei wird das Leerzeichen durch "#" ersetzt, da der Verbstamm als lexikalischer String betrachtet wird
            self.stem = stem[:-3].replace(" ","#")
        else:
            self.stem = stem.replace(" ","#")
        # die Verbbasis: Default ist immer Präsens
        self.base = "PRES"
        # Kausativvorkommen
        self.causativeOccurrences = 0
        # Basisfeatures
        self.baseFeatures = {
            # di-Vergangenheit als Feature (?DI-)
            "PAST":False,
            # Konditional als Feature (?SE-)
            "CONDfeature":False,
            # Inferentialis als Feature
            "INFER":False
        }
        # alle weiteren Features
        self.features = {
            # Reflexiv (N-)
            "REFL":False,
            # Reziprok (Ş-)
            "RECIP":False,
            # Kausativ (C-)
            "CAUS":False,
            # Passiv (L-)
            "PASS":False,
            # Negiert (M-)
            "NEG":False,
            # Potentialis (YEbil-)
            "POT":False,
            # Impotentialis (YEmE-)
            "IMPOT":False,
            # Interrogativ (#mI-)
            "INT":False,
            # Partizip
            "PART":False,
            # Person (Default: 3)
            "PERS":"3",
            # Numerus (Default: Singular)
            "NUM":"SG"
        }