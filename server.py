#Name: Luke James
#ID: 010930803

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

# Prepare to unpack data from client
##unpacker = struct.Struct('I 2s f')


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
                print('A!')
                response = f'Balance: ${balance}'
            
            # Withdraw
            elif command.startswith('b'):
                print('B!')
                amount = float(command.split()[1])
                if amount <= balance:
                    balance -= amount
                    response = f'Withdrawn: ${amount}'
                else:
                    response = 'Insufficient Funds'
            
            # Deposit
            elif command.startswith('c'):
                print('C!')
                amount = float(command.split()[1])
                balance += amount
                response = f'Deposited: ${amount}'
            
            # Quit
            elif command.startswith('d'):
                print('D!')
                break
            else:
                response = 'Invalid Request'

            # Send response back to client
            connectionSocket.send(response)

        connectionSocket.close()

    except:
        print('crashed!')
        exit(1)
    

# EXAMPLE WORK ===================================================================
# Print what we received in hex
            # print('received "%s"' % binascii.hexlify(data))
            # # Unpack the data back to what we need and print it # Note data is a tuple which is immutable in python (cannot change it)
            # unpacked_data = unpacker.unpack(data)
            # print('unpacked this from client')
            # print(unpacked_data)
            # print('')

            # # Convert to variables from tuple to show how to modify
            # print('Modifying data to send to client')
            # a, b, c = unpacked_data
            # a = a+1
            # # Note in Python 3 you need to do the "b"
            # b = b'cd'
            # c = c-1
            # # Put values in tuple and pack to send back to client
            # values = (a, b, c)
            # print(values)
            # packer = struct.Struct('I 2s f')
            # packed_data = packer.pack(*values)