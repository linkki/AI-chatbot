# Copyright (c) 2021 Veera Lupunen

from . import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def db_answer(word, i):
    sql = """SELECT content 
        FROM aicb.answer a 
        JOIN aicb.question_answer q_a 
        ON q_a.a_id = a.id
        WHERE q_a.q_id=(:word) 
        AND q_a.a_id=(:i)"""
        
    result = db.session.execute(sql, {"word":word, "i":i})
    answer = result.fetchone()[0]
    db.session.commit()
    
    return answer