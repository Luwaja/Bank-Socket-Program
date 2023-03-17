#Name: Luke James

# Import statements
import binascii
import struct
import sys
from socket import *

# Initialize account with $100
balance = 100

# Set passed in port number from client
serverPort = int(sys.argv[1])

# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM) # Choose SOCK_STREAM, which is TCP
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # The SO_REUSEADDR flag tells the kernel to reuse a local socket // in TIME_WAIT state, without waiting for its natural timeout to expire.

# Listening for client connections
serverSocket.bind(('', serverPort)) # Start listening on specified port
serverSocket.listen(1) # Listener begins listening

# Confirmation output
print('The server is ready to receive')
print('')

# APPLICATION ========================================================================================
# While loop loops indefinitely for client connections
while True:
    # Wait for connection and create a new socket, then output confirmation
    connectionSocket, addr = serverSocket.accept()
    print('Connection from', addr, 'accepted')
    print('')
    
    try:
        while True:
            # Receive request from client
            ##data = connectionSocket.recv(unpacker.size)
            command = connectionSocket.recv(1024).decode('utf-8')
        
            # Check balance
            if command.startswith('a'):
                response = f'====================\nYour balance is: ${balance}\n====================\n'
            
            # Withdraw
            elif command.startswith('b'):
                amount = float(command.split()[1])
                if amount < 0:
                    response = '====================\nThat is not a valid number.\n====================\n'
                elif amount <= balance:
                    balance -= amount
                    response = f'====================\nYou withdrew: ${amount}\n====================\n'
                else:
                    response = '====================\nYou dont have enough money.\n====================\n'
            
            # Deposit
            elif command.startswith('c'):
                amount = float(command.split()[1])
                balance += amount
                response = f'\n====================\nYou deposited: ${amount}\n====================\n'
            
            # Quit
            elif command.startswith('d'):
                break
            else:
                response = '====================\nInvalid Request\n====================\n'

            # Send response back to client
            connectionSocket.send(response.encode())

        connectionSocket.close()

    except:
        print('crashed!')
        exit(1)
