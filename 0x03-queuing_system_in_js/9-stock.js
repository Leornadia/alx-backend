// Required Modules
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Create Redis Client
const client = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create Express app
const app = express();
const PORT = 1245;

// Data - List of Products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Function to get item by id
function getItemById(id) {
  return listProducts.find((product) => product.itemId === id);
}

// Function to reserve stock by item id in Redis
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Function to get reserved stock by item id from Redis
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

// Route to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get details of a specific product by item id
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = reservedStock !== null
    ? product.initialAvailableQuantity - reservedStock
    : product.initialAvailableQuantity;

  res.json({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity,
    currentQuantity: currentQuantity
  });
});

// Route to reserve a product by item id
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId) || 0;

  if (reservedStock >= product.initialAvailableQuantity) {
    return res.json({ status: 'Not enough stock available', itemId: itemId });
  }

  await reserveStockById(itemId, reservedStock + 1);

  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

