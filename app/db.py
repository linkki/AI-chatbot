# Copyright (c) 2021 Veera Lupunen

from . import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy import text

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
    
def keywords():
    sql = text("SELECT word FROM aicb.question")
    result = db.session.execute(sql)
    
    keywords = result.fetchall()
    db.session.commit()
    
    keyword_set = set([
        x.word
        for x in keywords])
    
    return keyword_set
    
def fetch_id(word):
    sql = text("SELECT id FROM aicb.question WHERE word=(:word)")
    result = db.session.execute(sql, {"word":word})
    id = result.fetchone()[0]
    db.session.commit()
    
    return id
    
def fetch_answers(id):
    sql = text("""SELECT content 
        FROM aicb.answer a
        JOIN aicb.question_answer q_a 
        ON q_a.a_id = a.id
        WHERE q_id=(:id)""")
    
    result = db.session.execute(sql, {"id":id})
    answers = result.fetchall()
    db.session.commit()
    
    answer_list = [
        x.content
        for x in answers
    ]
    
    return answer_list
    
def check_code(code):
    "Returns 0 if code does not exist, 1 if code is a human code and 2 otherwise."
    sql = text("""SELECT human
        FROM aicb.code c
        WHERE c.id=(:code)""")
        
    result = db.session.execute(sql, {"code":code})
    answer = result.fetchone()
    db.session.commit()  
    
    if answer is None:
        return 0
    elif answer[0]:
        return 1
    else:
        return 2
    
    
    
    
    
