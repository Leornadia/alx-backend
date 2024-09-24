// Import redis client using ES6 syntax
import redis from 'redis';

// Create a Redis client for the subscriber
const client = redis.createClient();

// Log when the client is connected
client.on('connect', function () {
    console.log('Redis client connected to the server');
});

// Log any connection errors
client.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
client.on('message', function (channel, message) {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});

