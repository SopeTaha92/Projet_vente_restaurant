


CREATE TABLE vente_restaurant (
    order_id TEXT,
    restaurant TEXT,
    customer_name TEXT,
    order_date TEXT,
    order_time TEXT,
    menu_item TEXT,
    category TEXT,
    quantity TEXT,
    unit_price TEXT,
    discount TEXT,
    payment_method TEXT,
    rating TEXT
);

COPY vente_restaurant(
    order_id,
    customer_name,
    order_date,
    order_time,
    menu_item,
    category,
    quantity,
    unit_price,
    discount,
    payment_method,
    rating
)
FROM 'C:\Users\Mahmoud At-Tidianie\Desktop\GITHUB\Structuration_projet_vente-restaurant\data\raw\vente_restaurant.csv'
DELIMITER ','
CSV HEADER
ENCODING 'UTF8';

copy vente_restaurant(order_id, customer_name, order_date, order_time, menu_item, category, quantity, unit_price, discount, payment_method, rating)
FROM 'C:/Users/Mahmoud At-Tidianie/Desktop/GITHUB/Structuration_projet_vente-restaurant/data/raw/vente_restaurant.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM vente_restaurant;

\copy vente_restaurant(order_id, customer_name, order_date, order_time, menu_item, category, quantity, unit_price, discount, payment_method, rating)
FROM 'C:/Users/Mahmoud At-Tidianie/Desktop/GITHUB/Structuration_projet_vente-restaurant/data/raw/vente_restaurant.csv'
DELIMITER ','
CSV HEADER;
SHOW data_directory;

SELECT current_user;

-- Qui est le propriétaire de la table ?
SELECT table_name, table_schema, table_catalog
FROM information_schema.tables 
WHERE table_name = 'vente_restaurant';

GRANT ALL PRIVILEGES ON TABLE vente_restaurant TO sope;

GRANT ALL PRIVILEGES ON DATABASE vente_restaurant TO sope;
GRANT ALL PRIVILEGES ON TABLE vente_restaurant TO sope;
ALTER TABLE vente_restaurant OWNER TO sope;

INSERT INTO vente_restaurant VALUES 
    ('REST-001','paris_central','alice martin','15/03/2024','19:30','Pizza Margherita','PIZZA','1','12.50€','0%','CARD','5'),
    ('REST-002','LYON_SUD','BOB DUPONT','2024-03-16','20:15','BURGER CLASSIC','BURGER','2','15.00','10%','CASH','4'),
    ('REST-003','marseille_vieux_port','charlie legrand','17/03/2024','21:00','salade cesar','SALAD','1','9.80€','5%','CARD','4'),
    ('REST-004','LILLE_CENTRE','diana roy','2024-03-18','19:45','PASTA CARBONARA','PASTA','1','14.20€','0%','CARD','5'),
    ('REST-005','TOULOUSE_CAPITOLE','evelyn tremblay','19/03/2024','20:30','Steak frites','MAIN COURSE','1','18.50','15%','CASH','3'),
    ('REST-006','BORDEAUX_QUAIS','frank klein','2024-03-20','21:15','POISSON DU JOUR','FISH','1','22.00€','0%','CARD','5'),
    ('REST-007','NICE_PROMENADE','grace leroy','21/03/2024','19:00','PLAT VEGETARIEN','VEGETARIAN','2','16.80','10%','CARD','4'),
    ('REST-008','STRASBOURG_GRANDE_ILE','henry gauthier','2024-03-22','20:45','ASSIETTE FROMAGES','CHEESE','1','12.00€','5%','CASH','4'),
    ('REST-009','MONTPELLIER_ECUSSON','ivana petrov','23/03/2024','21:30','DESSERT MAISON','DESSERT','3','6.50€','20%','CARD','5'),
    ('REST-010','RENNES_CENTRE','jack wilson','2024-03-24','19:15','CAFE GOURMAND','DESSERT','2','8.00','0%','CARD','4'),
    ('REST-011','paris_central','sophie bernard','25/03/2024','20:00','Pizza Margherita','PIZZA','1','12.50€','0%','CASH','5'),
    ('REST-012','LYON_SUD','lucas moreau','2024-03-26','21:45','BURGER CLASSIC','BURGER','2','15.00','10%','CARD','4');

SELECT COUNT(*) 
FROM information_schema.columns 
WHERE table_name = 'vente_restaurant';

ALTER TABLE vente_restaurant ADD COLUMN restaurant TEXT;

SELECT * from vente_restaurant;

DROP TABLE vente_restaurant;