# Inventory CRUD API

1. Project title: Inventory Manager

## 📌 Description
A FastAPI project with full CRUD operations for managing an inventory system with MySQL.

## 🚀 Setup Instructions

1. Clone this repo
2. Create a MySQL database named `inventory_db`
3. Run `sql/init.sql` to create tables
4. Update credentials in `db.py`
5. Install packages: `pip install -r requirements.txt`
6. Run the app: `uvicorn main:app --reload`

## 🛠 API Endpoints
- `GET /products` – List all products
- `POST /products` – Add a new product
- `PUT /products/{id}` – Update product
- `DELETE /products/{id}` – Delete product

## Entity Relationship Diagram (ERD)

![ERD][def]


[def]: https://github.com/Mnce0415/inventory-api/raw/main"C:\Users\franc\PLP Full stack\Database (MySQL)\Screenshot.png"