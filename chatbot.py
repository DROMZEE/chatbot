# -*- coding: utf-8 -*-

import re
import random
import string

# Les input
q_bonjour = r"salut.*|bonjour.*|coucou.*|hello.*"
q_ca_va = r"comment vas-tu.*|ca.*va.*|quoi de neuf.*|"
q_nom = r"quel est ton nom.*|tu t'appelles comment.*|.*(ton) nom\??"
q_age = r".*?ton (age|âge).*|.*?quel (age|âge).*?"
q_chanson = r"tu écoutes quoi.*|.*(musique|chanson).*(aimes?|preferes?|préférée?)"
q_habitation = r"tu (habites|vis) (où|ou).*|(.*?(ou|où) habite.*?(tu|vous).*?)|(ou|où) tu (habites|habite).*"
q_emploi = r"tu fais quoi.*|tu travailles dans quoi.*|quel ton job.*"
q_good_by = r"au revoir|quit|ciao|hasta la vista|à \+"
q_meteo = r"quel temps fait-il à .*?|.*météo à .*?"

# les output
msg_bot = ["bonjour", "salut"]
msg_ca_va = ["super", "bien", "très bien, merci"]
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

# Comment ça va ?
    elif (re.fullmatch(q_ca_va, text_user)):
        print(random.choice(msg_ca_va))
# quel est ton nom ?
    elif (re.fullmatch(q_nom, text_user)):
        print(random.choice(msg_nom))
# quel age ?
    elif (re.fullmatch(q_age, text_user)):
        print(random.choice(msg_age))
# chanson pref ?
    elif (re.fullmatch(q_chanson, text_user)):
        print(random.choice(msg_chanson))
# habitation ?
    elif (re.fullmatch(q_habitation, text_user)):
        print(random.choice(msg_habitation))
# job
    elif (re.fullmatch(q_emploi, text_user)):
        print(random.choice(msg_emploi))
# météo
    elif (re.search(q_meteo, text_user)):
        text_user = re.sub(f"[{string.punctuation}]", " ", text_user)
        print(f"Il fait beau à {text_user.split()[-1]}")
# question inconnue
    else:
        print(random.choice(msg_inconnu))