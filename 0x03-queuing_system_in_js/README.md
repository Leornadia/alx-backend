# 0x03. Queuing System in JS

## Redis Setup and Key-Value Storage

### Steps to Run Redis:
1. Download and compile Redis 6.0.10.
    ```bash
    $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    $ tar xzf redis-6.0.10.tar.gz
    $ cd redis-6.0.10
    $ make
    ```

2. Start Redis in the background:
    ```bash
    $ src/redis-server &
    ```

3. Set and get a key in Redis:
    ```bash
    $ src/redis-cli set Holberton School
    $ src/redis-cli get Holberton
    ```

4. Kill Redis server:
    ```bash
    $ ps aux | grep redis-server
    $ kill [PID_OF_Redis_Server]
    ```

5. Copy the `dump.rdb` file into the project root.
    ```bash
    $ cp /path/to/redis-5.0.7/dump.rdb /path/to/your/queuing_project/
    ```

Running `get Holberton` in the Redis client should return `School`.

