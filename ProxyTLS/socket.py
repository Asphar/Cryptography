import signal
import socket
import threading
import sys

config = {
    "HOST_NAME" : "127.0.0.1",
    "BIND_PORT" : 8888,
    "MAX_REQUEST_LEN" : 1024,
    "CONNECTION_TIMEOUT" : 5
}

class Server:

    def __init__(self, config):
        # Creating a socket serverSocket of the server class.
        # This creates a socket for the incoming connections.
        # We then bind the socket and then wait for the clients to connect.

        signal.signal(signal.SIGINT, self.shutdown)

        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to a public host and a port
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))

        self.serverSocket.listen(10) # Become a server socket
        self.__clients = {}

        while True:
            # Wait for the client's connection request and once a successful connection is made, 
            # dispatch the request in a separate thread, making ourselves available for the next request.
            # This allows us to handle multiple requests simultaneously which boosts the performance of the server multifold times.

            # Establish the connection
            (clientSocket, client_address) = self.serverSocket.accept()

            d = threading.Thread(name=self._getClientName(client_address), target = self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()

        
        # Fetch the data from source and then pass it to the client

        # Get the request from browser 
        request = conn.recv(config['MAX_REQUEST_LEN'])

            # Parse the first line
        first_line = request.split('\n')[0]
            
        # Get url
        url = first_line.split(' ')[1]

        # Find the destination address of the request.
        # Address is a tuple of (destination_ip_address, destination_port_no)

        http_pos = url.find("://") # Find pos of ://
        if (http_pos == -1):
            temp = url
        else:
            temp = url[(http_pos+3):] # Get the rest of url

        port_pos = temp.find(":") # Find the port pos (if any)

        # Find end of web server
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos == -1 or webserver_pos < port_pos):
            # Default port
            port = 80
            webserver = temp[:webserver_pos]

        else: # Specific port
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]

        # Setup a new connection to the destination server (or remote server)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(config['CONNECTIONS_TIMEOUT'])
        s.connect((webserver, port))
        s.sendall(request)


        # The server's response is redirected to the client.
        # conn is the original connection to the client.
        # The response may be bigger then MAX_REQUEST_LEN that we are receiving in one call

        while 1:
            # Receive data from web server
            data = s.recv(config['MAX_REQUEST_LEN'])

            if (len(data) > 0):
                conn.send(data) # Send to browser/client

            else:
                break

# For the test
"""
1. Run the server on a terminal. Keep it running and switch to your favorite browser.
2. Go to your browser's proxy settings and change the proxy server to 'localhost' and port to '12345'
3. Now open any HTTP website (not HTTPS), for eg. geeksforgeeks.org and it's done ! 
   You should be able to access the content on the browser.

   We would be adding the following features in our proxy server :
   - Blaclisting domains
   - Content monitoring
   - Logging
   - HTTP Webserver + ProxyServer
"""
