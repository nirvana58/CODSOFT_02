import random
import string

def generate_password(length):
  Alphabets=string.ascii_letters 
  Numbers=string.digits 
  Symbols=string.punctuation 
  characters = Alphabets+Numbers+Symbols
  password = ''.join(random.choice(characters) for i in range(length))
  return password

try:
  length = int(input("Enter the desired password length: "))
  password = generate_password(length)
  print("Your generated password is:", password)
except ValueError:
  print("Invalid input. Please enter a number.")
