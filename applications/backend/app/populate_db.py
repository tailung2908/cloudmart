# populate_db.py
from app.database import SessionLocal, engine, Base
from app import models

# Make sure the tables exist
Base.metadata.create_all(bind=engine)

# Create a session
db = SessionLocal()

# Sample products
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": 3, "name": "Coffee Mug", "category": "Kitchen", "price": 12.99},
]

# Insert products into the database
for p in products:
    product = models.Product(**p)
    db.add(product)

# Commit and close
db.commit()
db.close()

print("Database populated with sample products!")
