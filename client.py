import socket # importing python socket module
import random # used for random number generation

client = socket.socket() # creating client socket

client.connect(('localhost', 9999)) # connecting socket to localhost ip and port number 9999

key_length = int(input("\nPlease choose a key length (8-64): ")) # key length user input
while key_length > 64 or key_length < 8:
    print("The key length must be between 8-64\n")
    key_length = int(input("Please choose a key length (8-64): "))  # key length user input

# ------ sending the authentication key length to the server ------ #
client.send(bytes(str(key_length), 'utf-8'))

# some_data = input("Enter some data to send to the server: ")

line_num = random.randint(1,50) # randomly selecting a line number 1-100

file = open('image_data.txt') # opening image data file

data = file.readlines() # reading contents of the image data file

list = [] # creating list for data to be entered into

list.append(data[line_num]) # appending line from file into list

def split(word):
    return [char for char in word.strip()]

split_list = []
for word in list:
    split_list.extend(split(word))

#print(split_list) # print entire random line of text file for testing

counter = 0 # counter to iterate through the list elements
auth_key = [] # creating list for final authentication key to be entered into

for x in range (key_length): # starting loop
    #print(split_list[counter]) # printing each element for testing
    auth_key.append(split_list[counter]) # appending each element to new list auth_key
    counter += 1 # adding 1 to the counter to move element position up by 1

print("\nThe key length is: " +str(key_length))  # making clearer to user
print("The final authentication key is: " + str(auth_key)) # making clearer to user

client.send(bytes(str(auth_key), 'utf-8'))

print("\nThe server replied: " + client.recv(1024).decode())
print("\nThe server replied: " + client.recv(1024).decode())
print("The server replied: " + client.recv(1024).decode())
