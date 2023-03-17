#Name: Luke James

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
    print('')
     
    # Send request to server
    clientSocket.send(command.encode('utf-8'))

    # Receive the response from the server
    response = clientSocket.recv(1024).decode('utf-8')

    # Print response
    print(response)

    # End the program if the user chooses 'Quit'
    if command.startswith('d'):
        print('Quitting the program. Come again!')
        break

clientSocket.close()
