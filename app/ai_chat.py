# Copyright (c) 2021 Veera Lupunen

#Odota, että oppilaalta tulee viesti
#Lue viesti ja hae tietokannasta satunnainen vastaus
#Laske vastauksen pituus, odota tietty sekuntimäärä ja lähetä viesti oppilaalle

import random
from .db import keywords, fetch_id, fetch_answers

def ai_answer(message):
    set = keywords()
    words = message.split()
    
    for w in words:
        w = w.casefold()
        if w in set:
            id = fetch_id(w)
            
            answers = fetch_answers(id)
            i = random.randint(0, len(answers)-1)
            
            return answers[i]
        else:
            return "Heipä hei! (olen tekoäly)"

    