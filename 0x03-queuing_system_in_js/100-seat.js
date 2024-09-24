const express = require('express');
const redis = require('redis');
const kue = require('kue');
const util = require('util');

const app = express();
const port = 1245;

// Redis Client
const client = redis.createClient({
  host: 'localhost', // Adjust if your Redis is on a different host
  port: 6379, // Default Redis port
});

// Promisify Redis methods
client.getAsync = util.promisify(client.get).bind(client);
client.setAsync = util.promisify(client.set).bind(client);

// Kue Queue
const queue = kue.createQueue();

// Global variables
let reservationEnabled = true;

// Redis functions
const reserveSeat = async (number) => {
  await client.setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const seats = await client.getAsync('available_seats');
  return parseInt(seats, 10);
};

// Initialize Redis
(async () => {
  await reserveSeat(50);
})();

// Express routes
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {});
  job.save((err) => {
    if (err) {
      console.log('Error adding job:', err);
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const availableSeats = await getCurrentAvailableSeats();
      const newSeats = availableSeats - 1;

      await reserveSeat(newSeats);
      console.log(`Seat reservation job ${job.id} completed`);

      if (newSeats === 0) {
        reservationEnabled = false;
      }
      done(null, 'Job completed'); 
    } catch (err) {
      console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
      done(err);
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
