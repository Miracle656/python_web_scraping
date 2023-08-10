# Loading the lowercase alphabet to a list
import string
alpha_1= list(string.ascii_lowercase)
print(f"{alpha_1}\n")

#reverse the list
alpha_2 = alpha_1[::-1]
print(f"{alpha_2}\n")

#create a dictionary from the 2 list
alpha_dict = {}

for i in alpha_1:
	for j in alpha_2:
		alpha_dict[i] = j
		alpha_2.remove(j)
		break
	
print(f"{alpha_dict}\n")

for i in alpha_dict:
	print(f"{i} : {alpha_dict[i]}")
	
#raw message	
message = "Theres no need for war between Niger and Nigeria both countries should find a way to settle without war"

print(f"\n{message}")

#encrypt the message using ceaser_ cipher
ciphered_message = ""

for i in message.lower():
	ciphered_message += alpha_dict.get(i," ")

print(f"\n{ciphered_message}")