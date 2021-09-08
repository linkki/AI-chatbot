# Copyright (c) 2021 Veera Lupunen

#Odota, että oppilaalta tulee viesti
#Lue viesti ja hae tietokannasta satunnainen vastaus
#Laske vastauksen pituus, odota tietty sekuntimäärä ja lähetä viesti oppilaalle

import random, time
from .db import keywords, fetch_id, fetch_answers

def ai_answer(message):
    if message == "":
        time.sleep(3)
        return "Mitä haluaisit kysyä seuraavaksi?"
        
    keywords_from_db = keywords()
    words = message.split()
    
    for w in words:
        w = w.casefold()
        if w in keywords_from_db:
            id = fetch_id(w)
            
            answers = fetch_answers(id)
            i = random.randint(0, len(answers)-1)
            
            answer = answers[i]
            
            time.sleep(len(answer)/10 + random.randint(0,3))
            return answer
        else:
            time.sleep(1)
            return "Heipä hei! (olen tekoäly)"

    