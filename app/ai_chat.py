# Copyright (c) 2021 Veera Lupunen

#Odota, että oppilaalta tulee viesti
#Lue viesti ja hae tietokannasta satunnainen vastaus
#Laske vastauksen pituus, odota tietty sekuntimäärä ja lähetä viesti oppilaalle

import random
from .db import db_answer

def ai_answer(message):
    #Hae avainsanat tietokannasta --> hashmapiin tms. --> fiksaa alla oleva
    #Etsi avainsanaa TODO: loput vaihtoehdot
    if "miksi" in message:
        i = random.randint(1,4)
        return db_answer(1, i)
    else:
        return "Heipä hei! (olen tekoäly)"

    