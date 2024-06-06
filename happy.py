import cv2
import os
import string

# Read the image
img = cv2.imread("happy.jpg")
msg = input("Enter secret message: ")
password = input("enter password: ")

# Create ASCII encoding dictionaries
a = {}
b = {}
for i in range(255):
    a[chr(i)] = i
    b[i] = chr(i)

# Initialize counters for rows, columns, and color channels
r = 0
c = 0
z = 0

# Embed the message into the image
for i in range(len(msg)):
    img[r, c, z] = a[msg[i]]
    r = r + 1
    c = c + 1 
    z = (z + 1) % 3

# Save the modified image
cv2.imwrite("encryptedImage.jpg", img)
# Open the modified image
os.startfile("encryptedImage.jpg")

message = " "
r = 0
c = 0
z = 0
pas = input("enter password for decryption: ")
if(password == pas):
    # Extract the message
    for i in range(len(msg)):
        message = message + b[img[r, c, z]]
        r = r + 1
        c = c + 1  
        z = (z + 1) % 3
    print("Decrypted message is: ", message)
else:
    print("you're not an authorized person")
