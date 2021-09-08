# Copyright (c) 2021 Veera Lupunen

#Odota, että oppilaalta tulee viesti
#Lue viesti ja hae tietokannasta satunnainen vastaus
#Laske vastauksen pituus, odota tietty sekuntimäärä ja lähetä viesti oppilaalle

import random
from .db import db_answer, keywords, fetch_id, fetch_answers

def ai_answer(message):
    set = keywords()
    words = message.split()
    
    for w in words:
        w.lower()
        if w in set:
            #hae avainsanan id tietokannasta
            id = fetch_id(w)
            
            """hae sanaan liitettyjen vastausten lukumäärä --> voiko yhdistää edelliseen?
            a_count = count_answers(id)
            i = random.randint(1,a_count)"""
            
            answers = fetch_answers(id)
            i = random.randint(0, len(answers)-1)
            
            return answers[i]
        else:
            return "Heipä hei! (olen tekoäly)"

    