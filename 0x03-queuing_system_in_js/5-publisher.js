// Import redis client using ES6 syntax
import redis from 'redis';

// Create a Redis client for the publisher
const client = redis.createClient();

// Log when the client is connected
client.on('connect', function () {
    console.log('Redis client connected to the server');
});

// Log any connection errors
client.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message to the channel after a delay
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message);
    }, time);
}

// Call the function with different messages and delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);

