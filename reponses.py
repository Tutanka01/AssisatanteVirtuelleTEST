import random

def ça_va():
    rep = ["Oui ça va tres bien",
            "Merci pour demander je vais tres bien",
            "En ce moment ça va",
            "Oui assez bien",
            "Niquel comme toujours"]
    rep = random.choice(rep)
    return rep

def et_vous():
    rep = ["Et vous comment vous allez?",
            "Merci pour avoir demande et vous?",
            "Et si on parlait de vous?",
            "J'espere que vous allez bien aussi"]
    rep = random.choice(rep)
    return rep
    
def finale():
    rep = ["Heureuse d'entendre ça",
            "C'est excellent",
            "J'espere que ça durera !"]
    rep = random.choice(rep)
    return rep