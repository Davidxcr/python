
user_input = input("Please enter a String: ")
reverse_string = ""

for item in range(len(user_input) - 1, -1, -1):
    reverse_string += user_input[item]

print(reverse_string)