-- CREATE DATABASE saleh


CREATE TABLE clients(
    client_id SERIAL PRIMARY KEY,
    Nom VARCHAR(50),
    Prénom VARCHAR(50),
    Age SMALLINT,
    Adresse TEXT,
    Mail VARCHAR(100)
);

INSERT INTO clients (Nom, Prénom, Age, Adresse, Mail) 
VALUES ('saleh' , 'Mahmoud', 24, 'Dahra', 'hdkqd');

INSERT INTO clients (Nom, Prénom, Age, Adresse, Mail) 
VALUES ('Saleh', 'Mahmoud', 24, 'Dahra', 'mahmoud@email.com');


INSERT INTO clients (Nom, Prénom, Age, Adresse, Mail) VALUES
('Ndiaye', 'Abdoulaye', 28, 'Dakar', 'abdou.ndiaye@email.sn'),
('Diop', 'Fatou', 34, 'Saint-Louis', 'fatou.diop@email.sn'),
('Fall', 'Ibrahima', 22, 'Thiès', 'ibra.fall@email.sn'),
('Sow', 'Awa', 45, 'Mbour', 'awa.sow@email.sn'),
('Gueye', 'Moussa', 31, 'Dakar', 'moussa.gueye@email.sn'),
('Kane', 'Mariam', 27, 'Ziguinchor', 'mariam.kane@email.sn'),
('Diallo', 'Oumar', 52, 'Kaolack', 'oumar.diallo@email.sn'),
('Ba', 'Khadija', 24, 'Dakar', 'khadija.ba@email.sn'),
('Seck', 'Ousmane', 39, 'Touba', 'ousmane.seck@email.sn'),
('Thiam', 'Sokhna', 21, 'Dakar', 'sokhna.thiam@email.sn'),
('Faye', 'Babacar', 48, 'Fatick', 'babacar.faye@email.sn'),
('Sarr', 'Astou', 33, 'Dakar', 'astou.sarr@email.sn'),
('Diao', 'Alpha', 26, 'Kolda', 'alpha.diao@email.sn'),
('Mbow', 'Aminata', 41, 'Louga', 'ami.mbow@email.sn'),
('Wade', 'Lamine', 37, 'Dakar', 'lamine.wade@email.sn'),
('Sy', 'Cheikh', 30, 'Tivaouane', 'cheikh.sy@email.sn'),
('Cissé', 'Pape', 25, 'Dakar', 'pape.cisse@email.sn'),
('Ndao', 'Coumba', 29, 'Matam', 'coumba.ndao@email.sn'),
('Bodian', 'Souleymane', 43, 'Bignona', 'souley.bodian@email.sn'),
('Touré', 'Binetou', 32, 'Dakar', 'binetou.toure@email.sn'),
('Mané', 'Sadio', 31, 'Sédhiou', 'sadio.mane@email.sn'),
('Mbacké', 'Serigne', 55, 'Touba', 'serigne.mbacke@email.sn'),
('Samb', 'Ndèye', 23, 'Rufisque', 'ndeye.samb@email.sn'),
('Ly', 'Yaya', 47, 'Dakar', 'yaya.ly@email.sn'),
('Dramé', 'Adama', 20, 'Tambacounda', 'adama.drame@email.sn'),
('Camara', 'Sékou', 36, 'Dakar', 'sekou.camara@email.sn'),
('Sané', 'Yacine', 28, 'Ziguinchor', 'yacine.sane@email.sn'),
('Goudiaby', 'Jean', 34, 'Oussouye', 'jean.goudiaby@email.sn'),
('Diagne', 'Modou', 50, 'Dakar', 'modou.diagne@email.sn'),
('Mendy', 'Thérèse', 40, 'Dakar', 'therese.mendy@email.sn'),
('Niang', 'Khalil', 22, 'Thiès', 'khalil.niang@email.sn'),
('Badji', 'Omar', 44, 'Kolda', 'omar.badji@email.sn'),
('Baldé', 'Abdou', 27, 'Velingara', 'abdou.balde@email.sn'),
('Sagna', 'Fama', 35, 'Dakar', 'fama.sagna@email.sn'),
('Gning', 'Birame', 38, 'Mbour', 'birame.gning@email.sn'),
('Lo', 'Maguette', 29, 'Touba', 'maguette.lo@email.sn'),
('Ciss', 'Mame', 31, 'Dakar', 'mame.ciss@email.sn'),
('Ndiaye', 'Bamba', 46, 'Diourbel', 'bamba.ndiaye@email.sn'),
('Ka', 'Aïssatou', 25, 'Linguère', 'aissa.ka@email.sn'),
('Traoré', 'Bakary', 53, 'Kayes', 'bakary.traore@email.sn'),
('Seye', 'Khady', 24, 'Dakar', 'khady.seye@email.sn'),
('Diatta', 'Landing', 33, 'Ziguinchor', 'landing.diatta@email.sn'),
('Barry', 'Ibrahima', 42, 'Dakar', 'ibra.barry@email.sn'),
('Gueye', 'Soda', 26, 'Saint-Louis', 'soda.gueye@email.sn'),
('Ndour', 'Youssou', 60, 'Dakar', 'youssou.ndour@email.sn'),
('Diop', 'Abdou', 19, 'Louga', 'abdou.diop2@email.sn'),
('Sall', 'Macky', 58, 'Fatick', 'macky.sall@email.sn'),
('Sonko', 'Ousmane', 49, 'Ziguinchor', 'ousmane.sonko@email.sn'),
('Gomis', 'Isabelle', 37, 'Dakar', 'isa.gomis@email.sn'),
('Diedhiou', 'Karim', 28, 'Ziguinchor', 'karim.diedhiou@email.sn'); 


SELECT * FROM clients

SELECT * FROM clients WHERE age > 50

SELECT AVG(age) from clients

SELECT * FROM clients ORDER BY age 

SELECT * FROM clients ORDER BY age DESC

-- DROP TABLE IF EXISTS clients  Pour supprimer la table clients 

SELECT Adresse from clients --Pour voir tout les adresse des clients

SELECT DISTINCT Adresse from clients --Pour voir les adresse distingue des clients sans doublont

SELECT Adresse, COUNT(*) as Nombre_clients --Pour renommer la colonne qui compte les clients
from clients 
GROUP BY adresse --Comme un groupby de python 
ORDER BY Nombre_clients DESC --Pour faire un trie par ordre décroissant


SELECT Adresse, ROUND(AVG(age), 2) as age_moyen --AVG(age) pour calculer la moyenne de la colonne age 
from clients 
-- Si tu veux filtrer sur le texte ou les chiffres d'origine (Nom, Ville, Age individuel) $\rightarrow$ utilise WHERE.
WHERE Adresse = 'Dakar'
GROUP BY adresse --Comme un groupby de python 
HAVING AVG(age) > 20 -- Pour faire des filtres vu que le résultat est obtenu avec avg where ne peux pas etre utilisé d'ou l'utilisation de HAVING
-- Si tu veux filtrer sur un calcul (COUNT, AVG, SUM) $\rightarrow$ utilise HAVING.
ORDER BY age_moyen DESC --Pour faire un trie par ordre décroissant Ziguinchor


-- EXO 1 

SELECT client_id, Nom, Prénom, Mail, Adresse
from clients 
WHERE Adresse = 'Ziguinchor' AND age  < 30

-- EXO 2 

SELECT * from clients
WHERE Nom LIKE 'D%' -- Ici j'avais pas le mis le % raison pour laquelle j'y est un peu galéré

-- EXO 3

SELECT adresse, COUNT(Adresse) as total_clients, MIN(age) as plus_jeune, MAX(age) as plus_agé, round(AVG(age), 2) as age_moyen
FROM clients
GROUP BY adresse
ORDER BY total_clients DESC

-- EXO 4

 SELECT * from clients
 WHERE age BETWEEN 25 AND 35


-- EXO 5

SELECT Nom, age, 
    CASE WHEN age >= 30 THEN 'Adult' ELSE 'Jeune' END as Tranche_Age 
from clients

-- EXO 6

SELECT
    CASE WHEN age <= 30 THEN 'Adult' ELSE 'Sénior' END as Tranche_Age,
    COUNT(*) as nombre
from clients
GROUP BY Tranche_Age


-- Exercice A : Le Rapport de Segmentation Géo-Démographique

SELECT Adresse, COUNT(client_id) as total_clients, round(AVG(age), 1) as age_moyen
from clients
WHERE age BETWEEN 20 and 50
GROUP BY Adresse
HAVING COUNT(client_id) > 3 -- je m'étais tromper un peu ici en mettant having total_clients > 3
ORDER BY age_moyen DESC


--  Exercice B : Le Score de Priorité (Le "Case When" avancé)


SELECT nom, prénom, age , 
    CASE 
        WHEN adresse = 'Dakar' AND age > 40 THEN 'URGENT' 
        when adresse = 'Dakar' AND age <= 40 THEN 'MOYEN'
        when adresse = 'Saint-Louis' then 'Zone_Nord'
        when adresse = 'Louga' then 'Zone_Centre'
        when adresse = 'Ziguinchor' then 'Zone_Sud'
        ELSE  'BASSE'
    END as Priorite
from clients
ORDER BY 
    CASE WHEN adresse = 'Dakar' AND age > 40 then 1
    when adresse = 'Dakar' AND age <= 40 then 2
    when adresse = 'Saint-Louis' then 3
    when adresse = 'Louga' then 4
    when adresse = 'Ziguinchor' then 5
    ELSE 6 end ASC
    















-- carte ID , BAC , demande manuscrite add à Fall mairie de dakar