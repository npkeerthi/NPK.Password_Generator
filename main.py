
import random
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


npk='''                                       |
 ___  ___  ___  ___       ___  ___  ___|
|   )|   )|___ |___ |   )|   )|   )|   )
|__/ |__/| __/  __/ |/\/ |__/ |    |__/ 
|                                       '''


print(npk)
print("\nWelcome to the NpK_Password Generator!\n")
l= int(input("How many letters would you like in your password?\n"))
s= int(input(f"How many symbols would you like?\n"))
n= int(input(f"How many numbers would you like?\n"))

k=""
for a in range(0,l):
  rl=random.choice(let)
  k+=rl

for b in range(0,s):
  k+=random.choice(sym)

for c in range(0,n):
  k+=random.choice(num)

print("Easy Password :",k)
password=''.join(random.sample(k,len(k)))
print("Hard Password :",password)


# random.shuffle(k)
# print("Hard Password :",k)

# import random
# let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# l= int(input("How many letters would you like in your password?\n")) 
# s= int(input(f"How many symbols would you like?\n"))
# n= int(input(f"How many numbers would you like?\n"))

# k=[]   #change in here
# for a in range(0,l):
#   rl=random.choice(let)
#   k+=rl

# for b in range(0,s):
#   k+=random.choice(sym)

# for c in range(0,n):
#   k+=random.choice(num)

# # change from here
# print("Easy Password :",k)
# random.shuffle(k)
# print("Hard Password :",k)
 
# password=""
# for i in k:
#   password+=i

# print(f"Your strong password :{password}")