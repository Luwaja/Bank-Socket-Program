#Name: Luke James
#ID: 010930803

# Import statements
import binascii
import struct
import sys
from socket import *

# Take hostname and port number as sting arguments from the command line
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))


# APPLICATION ========================================================================================
# Loop to get user input and send command to server
while True:
    # Take user input
    command = input('Enter a command \na) Check Balance \nb) Withdraw (amount) \nc) Deposit (amount) \nd) Quit \nInput: ')

    # Send request to server
    clientSocket.send(command.encode('utf-8'))

    # Receive the response from the server
    response = clientSocket.recv(1024).decode('utf-8')

    # Print response
    print(response)

    # End the program if the user chooses 'Quit'
    if command.startswith('Quit'):
        break

clientSocket.close()



# EXAMPLE WORK ===================================================================
# # Create values, format them, then pack them
# values = (1, b'ab', 2.7) # Send an integer, a two-character string, and a float # The variable values is a tuple in python. It is immutable # Note in Python 3 you have to do the "b" to cast the variable
# packer = struct.Struct('I 2s f') # Format = Integer 2strings float
# packed_data = packer.pack(*values) # Packs the values


# try:
#     # Print packed data
#     print('Values to send to server (before packing)')
#     print(values)
#     print('sending "%s" to server' % binascii.hexlify(packed_data))
#     print(' ')
#     # Send packed data
#     clientSocket.send(packed_data)

# except(RuntimeError, TypeError, NameError):
#     print('Crashed!')
#     exit(1)

# # Prepare to unpack data from server
# unpacker = struct.Struct('I 2s f')

# # Receive data from socket
# data = clientSocket.recv(unpacker.size)
# # Print what we received in hex. This is packed data
# print('received "%s" from server' % binascii.hexlify(data))
# # Unpack the data back to what we need and print it
# unpacked_data = unpacker.unpack(data)
# print('unpacked from server')
# print(unpacked_data)

# clientSocket.close()
