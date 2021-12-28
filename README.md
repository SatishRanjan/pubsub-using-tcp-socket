# Basic publisher subscriber using TCP socket
Publisher subscriber using tcp server and client socket

- Default server port: 8001
- Default server host: localhost

##### Dependencies
- Python version >= 3.0

**High Level Design:**

![alternativetext](/pubsub_client_server.png)


**How to run:**
- Clone repo
- Navigate to the cloned code folder
- Run pubsub server pubsub_server.py (option parameters [server_host] and [server_port]), starting server also starts a test event publisher thread that keeps publishing test event every 5 seconds
- Run event subscriber pubsub_client.py (option parameters [server_host] and [server_port]), multiple clients can connect-disconnect to the publisher
