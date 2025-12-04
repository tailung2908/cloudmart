// server.js
const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 8000;

// Enable CORS for all origins (development)
app.use(cors());

// Sample product data
const products = [
  { id: 1, name: 'Laptop', category: 'Electronics', price: 999.99 },
  { id: 2, name: 'Headphones', category: 'Electronics', price: 199.99 },
  { id: 3, name: 'Coffee Mug', category: 'Kitchen', price: 12.99 },
];

// Routes
app.get('/api/v1/products', (req, res) => {
  res.json(products);
});

// Start server
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on http://0.0.0.0:${PORT}`);
});
