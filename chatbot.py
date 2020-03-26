# -*- coding: utf-8 -*-

import re
import random
import string

q_bonjour = r"salut.*|bonjour.*|coucou.*|hello.*"
q_ca_va = r"comment ça va.*|comment vas-tu.*|quoi de neuf.*|"
q_nom = r"quel est ton nom.*|tu t'appelles comment.*"
q_age = r"Quel est ton âge.*|tu as quel age.*"
q_chanson = r"quelle est ta chanson préférée.*|tu écoutes quoi.*|musique.*"
q_habitation = r"tu habites où.*|tu vis où.*"
q_emploi = r"tu fais quoi.*|tu travailles dans quoi.*|quel ton job.*"
q_good_by = r"au revoir|quit|ciao|hasta la vista|à \+"
q_meteo = r"quel temps fait-il à .*?|.*météo à .*?"


msg_bot = ["bonjour", "salut"]
msg_ca_va = ["super", "bien"]
msg_nom = ["Cédric", "Cédric Dromzée"]
msg_age = ["40 ans"]
msg_chanson = ["ce qui passe à la radio"]
msg_habitation = ["Capbreton", "dans les Landes"]
msg_emploi = ["Développeur Data IA"]
msg_fin = ["merci pour votre visite"]
msg_inconnu = ["posez une autre question"]

flag = True
print("""Bienvenue sur ce bot \n Écrivez votre question : \n
Dites moi au revoir pour quitter""")
while (flag == True):
    text_user = input("> ")
    text_user = text_user.lower()
    if (re.search(q_good_by, text_user)):
        print(random.choice(msg_fin))
        flag = False
    elif (re.fullmatch(q_bonjour,text_user)):
        print(random.choice(msg_bot))
    elif (re.fullmatch(q_ca_va, text_user)):
        print(random.choice(msg_ca_va))
    elif (re.fullmatch(q_nom, text_user)):
        print(random.choice(msg_nom))
    elif (re.fullmatch(q_age, text_user)):
        print(random.choice(msg_age))
    elif (re.fullmatch(q_chanson, text_user)):
        print(random.choice(msg_chanson))
    elif (re.fullmatch(q_habitation, text_user)):
        print(random.choice(msg_habitation))
    elif (re.fullmatch(q_emploi, text_user)):
        print(random.choice(msg_emploi))
    elif (re.search(q_meteo, text_user)):
        text_user = re.sub(f"[{string.punctuation}]", " ", text_user)
        print(f"Il fait beau à {text_user.split()[-1]}")
    else:
        print(random.choice(msg_inconnu))