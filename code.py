print("WELCOME TO THE PYPASSWORD GENERATOR")
import random
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','_']
user_alphabet=int(input("How many alphabets you like to have? "))
user_numbers=int(input("How many numbers you like to have? "))
user_symbols=int(input("How many symbols you like to have? "))
password=[]
for pas in range(1, user_alphabet+1):
    password+=random.choice(alphabets)
for pas in range(1, user_numbers+1):
    password+=random.choice(numbers)
for pas in range(1, user_symbols+1):
    password+=random.choice(symbols)
random.shuffle(password)
pypassword=" "
for n in password:
    pypassword+=n
print(f"Your password could be: {pypassword}")
