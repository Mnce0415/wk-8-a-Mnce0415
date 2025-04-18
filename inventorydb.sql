-- Database Creation
CREATE DATABASE Inventorydb;

USE Inventorydb;

-- Categories Table
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Suppliers Table
CREATE TABLE Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(255) UNIQUE
);

-- Products Table
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    supplier_id INT,
    quantity INT DEFAULT 0,
    unit_price DECIMAL(10, 2),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

-- Stock Transactions Table
CREATE TABLE Stock_Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    transaction_type ENUM('IN', 'OUT') NOT NULL,
    quantity INT NOT NULL,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Sample Data (Add 2–3 entries per table)
INSERT INTO Categories (name, description) VALUES
('Electronics', 'Devices and gadgets'),
('Office Supplies', 'Stationery and essentials');

INSERT INTO Suppliers (name, contact_email) VALUES
('TechHouse', 'support@techhouse.com'),
('StationeryHub', 'info@stationeryhub.com');

INSERT INTO Products (name, category_id, supplier_id, quantity, unit_price) VALUES
('Laptop', 1, 1, 10, 950.00),
('Printer Paper', 2, 2, 500, 3.50);

INSERT INTO Stock_Transactions (product_id, transaction_type, quantity) VALUES
(1, 'IN', 10),
(2, 'OUT', 100);
