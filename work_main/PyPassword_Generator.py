import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Witam Cie w PyPassword Generator!")
nr_letters= int(input("Ile liter chcesz mieć w haśle?\n")) 
nr_symbols = int(input(f"Ile znaków specjalnych chcesz mieć w haśle?\n"))
nr_numbers = int(input(f"Ile cyfr chcesz mieć w haśle?\n"))

password_list = []

for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"To jest twoje hasło :{password}")