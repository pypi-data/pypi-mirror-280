# server.py

###############
# Server Setup
###############

from module import *

def print_hello(client,payload):    
    print(client.ip)
    if payload == 'hello':
        client.send('user_msg', 'hello')
    if payload == 'bye':
        client.send('user_msg', 'goodbye')
        print('bye')
        
        #client.close_connection()

def print_bye(client,payload):
    client.send('user_msg', 'goodbye')

# Define Server Object
my_server = Server(('127.0.0.1', 8080), 5)

# Define Which server Functions should be allocated to what keyword
my_server.New_Function('user_msg', print_hello)
my_server.New_Function('bye', print_bye)

# Start Server
my_server.start(ping=True)