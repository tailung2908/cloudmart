from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # create app first

origins = [
    "http://localhost:5173",        # local dev
    "http://127.0.0.1:5173",
    "http://cloudmart-frontend:5173"  # container name + port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Product model (Pydantic)
class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float

# Fake product database
fake_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": 3, "name": "Coffee Mug", "category": "Kitchen", "price": 12.99}
]

# Endpoint to list all products
@app.get("/api/v1/products", response_model=List[Product])
def get_products():
    return fake_products

# Root endpoint
@app.get("/")
def root():
    return {"message": "CloudMart backend is running!"}
