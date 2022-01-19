# Copyright (c) 2021 Veera Lupunen

#Odota, että oppilaalta tulee viesti
#Lue viesti ja hae tietokannasta satunnainen vastaus
#Laske vastauksen pituus, odota tietty sekuntimäärä ja lähetä viesti oppilaalle

import random
from . import socketio
from .db import keywords, fetch_id, fetch_answers

def ai_answer(message):
    
    greetings = ["moi", "hei", "terve", "päivää vain", "moikka", "moro", "heipä hei", "päivää", "heippa"]
    impossible = ["Tuohon kysymykseen en kyllä osaa vastata. Kysyisitkö jotain muuta?", "Jaa, se onkin hyvä kysymys. Mitä mieltä itse olet?", "Nyt en oikein ymmärrä kysymystä.", "Tuota, jaa. En osaa sanoa.", "Hmm, nyt en ole ihan varma, mitä tähän pitäisi vastata.", "Nyt täytyy myöntää, etten tiedä vastausta tähän kysymykseen. Kysy jotain helpompaa?", "En kyllä yhtään tiedä!"]
    
    message = message.casefold().rstrip("? .,!")
    
    if len(message) < 3:
        socketio.sleep(5)
        return "Mitä haluaisit kysyä seuraavaksi?"
    
    for greeting in ["miten menee", "mitä kuuluu"]:
        if greeting in message:
            return "Ihan hyvää kuuluu. Mitä sinulle kuuluu?"
        
    keywords_from_db = keywords()
    words = message.split()
    
    for ww in words:
        w = ww.rstrip("? .,!")
        if w in keywords_from_db:
            id = fetch_id(w)            
            answers = fetch_answers(id)
            i = random.randint(0, len(answers)-1)
            answer = answers[i]

            socketio.sleep(len(answer)/10 + random.randint(0,3))
            return answer

    for ww in words:
        w = ww.rstrip("? .,!")
        if w in greetings:
            i = random.randint(0, len(greetings)-1)
            answer = (greetings[i] + "!").capitalize()
            
            socketio.sleep(len(answer)/10 + random.randint(0,3))
            return answer

    i = random.randint(0, len(impossible)-1)
    answer = impossible[i]
    
    socketio.sleep(len(answer)/10 + random.randint(0,3))
    return answer
        
        