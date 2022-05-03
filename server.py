import socket # importing python socket module

server = socket.socket() # creating server socket
print('\nSocket Created') # informing user that socket has been created

server.bind(('localhost', 9999)) # binding socket to localhost ip and port number 9999

server.listen(5) # listening for connections from client
print('Waiting for connections from the client . . .') # informing user that the server is listening for connections

while True: # while listening do the following
    client, address = server.accept() # accept connection from client with correct IP and port

    print("\nConnected with client: ", address) # informing user of connection and showing IP address

    key_length = client.recv(1024).decode() # receiving data from client

    #client.send(bytes('Thank you for sending some data to me!', 'utf-8')) # sending client a welcome message

    print("\nThe received key length is: " + key_length) # printing the received data from client

    auth_key = client.recv(1024).decode()  # receiving data from client

    print("The received key is: " + auth_key)  # printing the received data from client

    #auth_key_length = []

    print("The length of the authentication key is: " +str(len(auth_key.split())))

    # checking that the initial key length matches the length of authentication key
    final_length = len(auth_key.split())
    if int(final_length) == int(key_length): # if they do match
        print("\nAuthentication Successful")

        client.send(bytes('Authentication Successful', 'utf-8'))
        client.send(bytes('My position is: x', 'utf-8'))
        client.send(bytes('My speed is: y', 'utf-8'))

    else: # if they do not match
        print("Authentication unsuccessful, closing connection. ")
        client.close()  # closing connection

    client.close() # closing connection
