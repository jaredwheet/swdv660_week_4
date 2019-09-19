# See readme for the instructions to run this application

import socket

HOST = '127.0.0.1' 
PORT = 9500      

#This method is the logic behind the application on the server side 
def runSocketProgram():    
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((HOST, PORT))    
    connection.listen()
    #The assignment asked to use port 9500
    print("Listening on port 9500")
    #To help users understand the next step
    print("Run client.py in a different command line to continue!!")

    #This basically loops and allows the application to keep going until CLOSE is typed to end the close the server connection
    runServer = True
    while runServer:
        
        session, addr = connection.accept()        
        receivedData = session.recv(1021).decode() 
        #Will always return goodbye... unless HELLO is the input from the user        
        serverResponse = "Goodbye"        
        if receivedData == "HELLO":
            serverResponse = "Hi"
        
        session.send(serverResponse.encode())        
        session.close()

runSocketProgram()