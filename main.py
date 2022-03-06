from calendar import calendar
import imp
from subprocess import list2cmdline
from quico import * # Le calendrier Google
import speech_recognition as sr
import pyttsx3
import wikipedia
import time
import webbrowser
import os
import asyncio
import pyjokes
from datetime import datetime
from meteo import *
from reponses import *

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
wikipedia.set_lang("fr")
temps = datetime.now()
engine = pyttsx3.init('sapi5')

def dire(audio):
    engine.say(audio)
    engine.runAndWait()
# Reading Microphone as source
# listening the speech and store in audio_text variable
def vocal():
    a = True
    a_faire = []
    faites = []
    while a:
        with sr.Microphone() as source:
            dire("Parlez")
            print("Parlez")
            audio_text = recognizer.listen(source) 
            dire("C'est bon")
            print("Tais toi")
            texte = recognizer.recognize_google(audio_text,language="fr-FR")
            print(texte)
            if texte == "ajouter à faire":
                with sr.Microphone() as source:
                    dire("Que voulez vous ajouter a votre liste?")
                    print("Que voulez vous ajouter a votre liste?")
                    audio_text = recognizer.listen(source)
                    texte = recognizer.recognize_google(audio_text,language="fr-FR")
                    print("D'accord "+texte+" a ete rajoute a votre liste")
                    dire("D'accord "+texte+" a ete rajoute a votre liste")
                    a_faire.append(texte)
            elif texte == "tâche fait":
                 with sr.Microphone() as source:
                    dire("Quelle tache a ete faite?")
                    audio_text = recognizer.listen(source)
                    texte = recognizer.recognize_google(audio_text,language="fr-FR")
                    dire("D'accord,",texte,"a ete enlevé de votre liste")
                    faites.append(texte)
                    a_faire.pop(texte)
            elif texte == "ma liste":
                 textestr = ''.join(str(e) for e in a_faire)
                 print("Votre liste de choses a faire est composé de : "+textestr)
                 dire("Votre liste de choses a faire est composé de "+textestr)
            elif "Wikipédia" in texte:
                with sr.Microphone() as source:
                    dire("Que voulez vous chercher sur wikipedia?")
                    audio_text = recognizer.listen(source)
                    texte = recognizer.recognize_google(audio_text,language="fr-FR")
                    print(texte)
                    resultat = wikipedia.summary(texte,sentences=2) #Le resultat sera donee en 2 lignes
                    print(resultat)
                    dire("Le resultat de votre recherch est : "+resultat) 
            elif "heure" in texte:
                heure_str = str(temps.hour)
                min_str = str(temps.minute)
                print("Il est "+heure_str+" heures")
                print("et "+min_str+"minutes")
                dire("Il est "+heure_str+" heures, et "+min_str+" minutes")
            elif "blague" in texte:
                dire("D'accord preparez votre ceinture pour ecouter cette blague!")
                print("D'accord preparez votre ceinture pour ecouter cette blague!")
                blague = pyjokes.get_joke(language = 'es')
                print(blague)
                dire(blague)
            elif "calendrier" in texte:
                try: # Voit si il y a un evenement
                    evenements = calendar2()
                    evenements = list(evenements) # Transforme le tuple evenement en liste
                    evenements.pop(0) # On supprime l'index 0 car il est compose de la date // Essayer de mettre aussi la date
                    evenements_str = ''.join(str(e) for e in evenements) # Liste a str
                    print(evenements_str)
                    dire("Prochainement vous avez : "+evenements_str)
                except: # Sinon renvoie ce messge
                    dire("Il n'y a pas d'evenements prochainement")
            elif "minuteur" in texte:       
                with sr.Microphone() as source:
                    dire("De combien de secondes voulez vous votre minuteur?") 
                    print("De combien de secondes voulez vous votre minuteur?")
                    audio_text = recognizer.listen(source)
                    texte = recognizer.recognize_google(audio_text,language="fr-FR")
                    dire("D'accord un chrono de "+texte+" secondes sera mis")
                    texte_int = int(texte)
                    for i in range(texte_int):
                        texte_str = str(texte_int)
                        dire(texte_str)
                        time.sleep(1)
                        texte_int -= 1
                        if texte_int == 0:
                            print("Fin")
                            dire("Fin de votre minuteur")
            elif "météo" in texte:
                try:
                    temp = temperature()
                    resen = temp_resentie()
                    nuage = nuages()
                    print("Aujourd'hui il fait "+temp+" degres avec un resentie de "+resen+" degres et une couverture nuageuse de "+nuage+" pourcent")
                    dire("Aujourd'hui il fait "+temp+" degres avec un resentie de "+resen+" degres et une couverture nuageuse de "+nuage+" pourcent")
                except:
                    print("Le service meteo ne fonctionne pas")
                    dire("Le service meteo ne fonctionne pas")

            elif "application" in texte:
                with sr.Microphone() as source:
                    print("Quelle application voulez vous ouvrir?")
                    dire("Quelle application voulez vous ouvrir?")
                    audio_text = recognizer.listen(source)
                    texte = recognizer.recognize_google(audio_text,language="fr-FR")
                    dire("D'accord j'ouvre "+texte)
                    print("D'accord j'ouvre "+texte)
                    if texte == "opéra":
                        os.startfile("C:/Users/Mohamad/AppData/Local/Programs/launcher.exe")
                    elif texte == "Steam":
                        os.startfile("D:/steam/Steam.exe")
            elif "ça va" in texte:
                dire(ça_va()) # Prend les reponses du fichier reponses.py
                time.sleep(1)
                with sr.Microphone() as source:
                    dire(et_vous())
                    audio_text = recognizer.listen(source)
                    texte = recognizer.recognize_google(audio_text,language="fr-FR")
                    dire(finale())
            elif "t'appelles" in texte:
                dire("Je m'appelle TEST par le moment.")
                print("Je m'appelle TEST par le moment.")
            elif "musique" in texte:
                with sr.Microphone() as source:
                    print("Quelle musique voulez vous chercher sur spotify?")
                    dire("Quelle musique voulez vous chercher sur spotify?")
                    audio_text = recognizer.listen(source)
                    texte = recognizer.recognize_google(audio_text,language="fr-FR")
                    dire("D'accord je vais chercher "+texte+" sur spotify")
                    webbrowser.open('https://open.spotify.com/search/{}'.format(texte))
                    
            elif texte == "tais-toi":
                a = False
            
            else:
                dire("Je n'ai rien a dire a ça")
vocal()

#Comment faire pour passer de liste a str :)
#list1 = [1, 2, 3]
#str1 = ''.join(str(e) for e in list1)