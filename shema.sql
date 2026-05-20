-- ============================================================================
-- Script de création des tables pour le pipeline Ventes Restaurant
-- ============================================================================

-- 1. Création de la table brute (Données sources)
CREATE TABLE IF NOT EXISTS vente_restaurant_12K_brute (
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

-- 2. Création de la table nettoyée et enrichie (Cible du pipeline ETL)
CREATE TABLE IF NOT EXISTS vente_restaurant_12K_clean (
    id SERIAL PRIMARY KEY,            
    order_id TEXT,
    restaurant TEXT CHECK (length(restaurant) <= 100),
    customer_name TEXT CHECK (length(customer_name) <= 150),
    order_date DATE,
    order_time TIME,
    menu_item TEXT CHECK (length(menu_item) <= 200),
    category TEXT CHECK (length(category) <= 100),
    quantity INTEGER CHECK (quantity > 0),
    unit_price NUMERIC(10, 2) CHECK (unit_price >= 0),          
    discount INTEGER CHECK (discount >= 0 AND discount <= 100),
    payment_method TEXT CHECK (length(payment_method) <= 50),
    rating INTEGER CHECK (rating >= 0 AND rating <= 5), 
    total_price NUMERIC(10, 2) CHECK (total_price >= 0),
    discount_amount NUMERIC(10, 2) CHECK (discount_amount >= 0),
    total_amount NUMERIC(10, 2) CHECK (total_amount >= 0),
    service_type TEXT CHECK (length(service_type) <= 20)       
);