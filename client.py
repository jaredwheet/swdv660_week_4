# See readme for the instructions to run this application

import socket

HOST = '127.0.0.1'  
PORT = 9500

#  This is where we will gather the input text from the user
def getUsersInput():
    print()
    print("Input is case sensitive")
    print("Type 'CLOSE' to close the connection to the server")    
    print("Otherwise, type anything else to send to the server!")
    print("HINT:  HELLO is a special word")
    print()
    usersInputString = input("Enter text here: ")
    print()
    print()
    return usersInputString

#This is the logic behind the application on the client side
def runSocketProgram():
    while True:
        socketInput = getUsersInput()

        if socketInput == "CLOSE":
            break
        
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((HOST, PORT))        
        connection.send(socketInput.encode())

        serverResponse = connection.recv(1021).decode()
        print("Response: " + serverResponse)

runSocketProgram()