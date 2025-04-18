# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint, condecimal, Field
from db import conn, cursor

app = FastAPI()

# Pydantic model with input validation
class Product(BaseModel):
    name: str
    quantity: conint(gt=0)  # Quantity must be greater than 0
    price: condecimal(gt=0)  # Price must be greater than 0

# GET all products
@app.get("/products")
def get_products():
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    return {"products": results}

# GET product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# POST create product
@app.post("/products")
def create_product(product: Product):
    cursor.execute(
        "INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)",
        (product.name, product.quantity, product.price)
    )
    conn.commit()
    return {"message": "Product created successfully!"}

# PUT update product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Product not found")
    cursor.execute(
        "UPDATE products SET name = %s, quantity = %s, price = %s WHERE id = %s",
        (product.name, product.quantity, product.price, product_id)
    )
    conn.commit()
    return {"message": "Product updated successfully!"}

# DELETE product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Product not found")
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    return {"message": "Product deleted successfully!"}
# Run the FastAPI app


