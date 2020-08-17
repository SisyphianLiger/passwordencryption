import random
import string
import secrets

#Stack Overflow website for initial pw generation
#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/23728630#23728630

def id_generator(size, chars=string.ascii_letters + string.digits):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for n in range(size))

def password_length():
    x = int(input("How many characters should your password be? "))
    return id_generator(x)

print(password_length())
