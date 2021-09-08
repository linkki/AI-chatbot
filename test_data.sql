-- Copyright (c) 2021 Veera Lupunen

BEGIN;

INSERT INTO question (word) VALUES('miksi'), ('miten'), ('oletko'), ('voisitko');

INSERT INTO answer (content) VALUES('Ehkä siksi että maapallo on pyöreä.'), ('Miksipä ei?'), ('Siksi, että muuten elämä voisi olla vaikeampaa.'), ('Voisiko vastaus olla evoluutio?');

INSERT INTO answer (content) VALUES('Voisit pyytää tähän apua vaikka kaveriltasi.'), ('Kannattaa etsiä netistä ohje. Sieltä varmaan löytyy neuvoja!'), ('Mitenköhän se menisi... Toimiskohan ihan kynä ja paperi?'), ('Vähän vaikea juttu. Miten itse lähtisit yrittämään?');

INSERT INTO answer (content) VALUES('Jaa, mitä itse arvaisit?'), ('En taatusti ole!'), ('Taidan olla.'), ('Tietysti olen :)');

INSERT INTO answer (content) VALUES('Tietty! Mitä siis pitäisi tehdä?'), ('En valitettavasti taida voida.'), ('Hmm, täytyy vähän miettiä. Mitä oikeastaan haluaisit että teen?'), ('Joo, toki. Kerro vain, mitä pitää tehdä.');

INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(1, 1);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(1, 2);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(1, 3);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(1, 4);

INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(2, 5);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(2, 6);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(2, 7);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(2, 8);

INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(3, 9);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(3, 10);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(3, 11);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(3, 12);

INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(4, 13);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(4, 14);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(4, 15);
INSERT INTO question_answer AS q_a (q_id, a_id) VALUES(4, 16);

-- lisää loput

COMMIT;
