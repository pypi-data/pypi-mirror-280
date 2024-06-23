# module.py

import socket
import threading
import time

### Module


#############
# Server side
#############
instances = []
clients = []

class Server:
    
    def __init__(self, address: tuple, max_clients: int = 5):
        self.address = address
        self.ip = address[0]
        self.port = address[1]
        self.max_clients = max_clients

    class Client:
        def __init__(self, client_socket, server):
            self.client_socket = client_socket
            self.ip = client_socket.getpeername()[0]
            self.server = server
            self.active = True
            self.last_ping_time = time.time()

        def send(self, keyword: str, payload: str):
            headers = [self.server.ip, self.ip]
            self.client_socket.send(f'{headers},{keyword},{payload}'.encode())
            print(f"sending '{keyword}: {payload}' to '{self.ip}'")

        def send_ping(self):
            try:
                headers = [self.server.ip, self.ip]
                ping = 'ping'
                self.client_socket.send(f'{headers},{ping},{""}'.encode())
                print(f"sending '{ping}' to '{self.ip}'")
            #     self.client_socket.settimeout(5.0)  # 5 seconds timeout for response
            #     response = self.client_socket.recv(1024)
            #     if response.decode().strip() == 'pong':
            #         self.active = True
            #     else:
            #         self.active = False
            # except socket.timeout:
            #     self.active = False
            except:
                 self.active = False

        def close_connection(self):
            self.client_socket.close()
            self.active = False

    def start(self, ping: bool = False):
        
        def handle_client(client_socket, addr, server):
            client = Server.Client(client_socket, server)
            
            def ping_thread(client):
                while client.active:
                    if time.time() - client.last_ping_time > 15:
                        client.active = False
                        client.close_connection()
                        print(f"Ping timeout, closing connection from {addr}")
                        break
                    elif time.time() - client.last_ping_time > 10 and time.time() - client.last_ping_time < 12:
                        client.send_ping()
                        time.sleep(2)
                    time.sleep(0.5)
                        

            if ping:
                threading.Thread(target=ping_thread, args=(client,), daemon=True).start()

            try:
                while client.active:
                    data = client_socket.recv(1024)
                    if data:
                        input_data = data.decode()
                        process_received_data(self,input_data,client)
            except Exception as e:
                print(e)
                clients.remove(threading.current_thread())
                client.close_connection()
        
        def process_received_data(self, received_data,client):
            
            try:
                
                parts = received_data.split(']', )
                headers = parts[0].strip('[').replace("'",'').split(', ')
                extracted_data = parts[1].strip(',')
                extracted_data = extracted_data.split(',',1)
                keyword = extracted_data[0]
                if len(extracted_data) > 1:
                    payload = extracted_data[1]
                else:
                    payload = ''

                if keyword == 'pong':
                    client.last_ping_time = time.time()  # Update the last ping time

                else:
                    # Check if the keyword is associated with a function
                    for instance in instances:
                        if instance.keyword == keyword:
                            instance.run(client=client,payload=payload)
                            break
                    else:
                        client_socket.send(f'{keyword} not recognized'.encode())

            except Exception as e:
                print(f"Received unexpected data format: {received_data}. Error: {e}")









        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(self.address)
        server_socket.listen(self.max_clients)
        print(f"Listening on {self.address} with max {self.max_clients} clients")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            thread_name = f'Thread-{len(clients) + 1} (handle_client)'
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, self), name=thread_name)
            clients.append(client_handler)
            client_handler.daemon = True
            client_handler.start()

    class New_Function:
        def __init__(self, keyword: str, function):
            self.keyword = keyword
            self.function = function
            instances.append(self) 
        
        def run(self, client,payload):
            return self.function(client,payload)
        
#############
# Client Side
#############

import socket
import threading
import time

client_functions = []

class Client:
    
    def __init__(self, address: tuple):
        self.address = address
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = socket.gethostbyname(socket.gethostname())  # Get client's IP address
        self.active = True
        self.on_connect_function = None
        self.last_ping_time = time.time()



    class Connected_Server:
        def __init__(self, address: tuple,client):
            self.address = address
            self.ip = address[0]
            self.port = address[1]
            self.client = client


        def send(self, keyword: str, payload: str):
            headers = [self.client.ip]
            self.client.client_socket.send(f'{headers},{keyword},{payload}'.encode())
            print(f"sending '{keyword}: {payload}' to '{self.ip}'")


        def close_connection(self):
            self.client.client_socket.close()
            self.client.active = False


    def connect(self, ping: bool = False):
        self.client_socket.connect(self.address)
        connected_server = self.Connected_Server(self.address,self)
        
        # Run the on_connect function if set
        if self.on_connect_function:
            self.on_connect_function(self)

        def check_ping_timeout():
            while self.active:
                if time.time() - self.last_ping_time > 15:
                    print("No ping received in the last 15 seconds, closing connection.")
                    self.active = False
                    self.close_connection()
                time.sleep(1)

        # Start the ping timeout check thread
        if ping:
            threading.Thread(target=check_ping_timeout, daemon=True).start()

        while self.active:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    received_data = data.decode().strip()
                    self.process_received_data(connected_server,received_data)
            except Exception as e:
                print(f"Error receiving or processing data: {e}")
                self.active = False
                self.close_connection()

    def process_received_data(self,connected_server, received_data):
        #the issue is here: the problem in my oppinion is that the server sends a ping every so often, but for whatever reason it sends it to all, probably because its the same ip but idk. So that might be a security thing anyway so when the client reconnects it just has like 800 requests to catch up on
        try:
            
            parts = received_data.split(']', )
            incoming_headers = parts[0].strip('[').replace("'",'').split(', ')
            extracted_data = parts[1].strip(',')
            extracted_data = extracted_data.split(',',1)
            incoming_keyword = extracted_data[0]
            if len(extracted_data) > 1:
                incoming_payload = extracted_data[1]
            else:
                incoming_payload = ''

            if incoming_keyword == 'ping':
                headers = [self.ip]
                self.client_socket.send(f'{headers},pong,'.encode())
                print(f"sending 'pong' to '{connected_server.ip}' [server]")
                self.last_ping_time = time.time()  # Update the last ping time

            else:
                # Check if the keyword is associated with a function
                for func in client_functions:
                    if func.keyword == incoming_keyword:
                        func.run(connected_server, incoming_payload)
                        break
                else:
                    print(f"Keyword '{incoming_keyword}' not recognized")

        except Exception as e:
            print(f"Received unexpected data format: {received_data}. Error: {e}")

            
    def send(self, keyword: str, payload: str):
        headers = [self.ip]
        self.client_socket.send(f'{headers},{keyword},{payload}'.encode())
        print(f"sending '{keyword}: {payload}' to server")

    def close_connection(self):
        self.client_socket.close()
        self.active = False

    class New_Function:
        def __init__(self, keyword: str, function):
            self.keyword = keyword
            self.function = function
            client_functions.append(self)
        
        def run(self, server, payload):
            return self.function(server, payload)

    def on_connect(self, function):
        self.on_connect_function = function  # Assign the function, will be called with self
