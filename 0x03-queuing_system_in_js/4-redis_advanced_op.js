// Import the redis library using ES6 syntax
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Listen for the 'connect' event to log a success message
client.on('connect', function () {
    console.log('Redis client connected to the server');
});

// Listen for the 'error' event to log an error message
client.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to create a hash in Redis
function createHolbertonSchoolsHash() {
    client.hset('HolbertonSchools', 'Portland', 50, redis.print);
    client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    client.hset('HolbertonSchools', 'New York', 20, redis.print);
    client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

// Function to display the hash stored in Redis
function displayHolbertonSchoolsHash() {
    client.hgetall('HolbertonSchools', (err, reply) => {
        if (err) {
            console.log(err);
        } else {
            console.log(reply); // Logs the entire hash object
        }
    });
}

// Call the functions
createHolbertonSchoolsHash();
displayHolbertonSchoolsHash();

