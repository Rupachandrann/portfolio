import random
letter = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
        'T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z')
number = ('0','1','2','3','4','5','6','7','8','9')
symbol = ('?','/',')','(','*','&','^','%','$','#','@','!')
print("__Welcome to generate to your new password!__\n\n")
n_number = int(input("How many number are there in enter the numbers ? \n==> "))# user get
n_letter = int(input("How many letter are there in enter the letter ? \n==> "))
n_symbol = int(input("How many symbol are there in enter the symbol ? \n==> "))
password = "____Your Amazing Password Is____\n\n"
for i in range(1,n_letter+1):# using loop statement with itrate the values
    char = random.choice(letter)# random pic the letter
    password += char # using assignment operater
for j in range(1,n_number+1): 
    num = random.choice(number)
    password += num
for k in range(1,n_symbol+1):
    sym = random.choice(symbol)
    password += sym
print(password)# to print the assign the value of password variable
