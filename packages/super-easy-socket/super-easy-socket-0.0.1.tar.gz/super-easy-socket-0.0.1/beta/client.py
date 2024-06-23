# client.py

from module import Client

# User-defined client functions
def on_server_msg(server,payload):
    print(f"Received message from server: {payload}") 
    if(payload == 'hello'):
        server.send('user_msg', 'goodbye')
        print(server.ip)
        #server.close_connection()
        print('bye')


def on_connect(server):  # Modify to accept client as an argument
    server.send('user_msg', 'hello')
    print("Connected to the server successfully!")

# Define Client Object
my_client = Client(('127.0.0.1', 8080))

# Define which client functions should be allocated to what keyword
my_client.New_Function('user_msg', on_server_msg)
my_client.on_connect(on_connect)

# Connect Client to Server
my_client.connect(ping=True)