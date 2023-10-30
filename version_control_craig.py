https://github.com/heathcraig/Version-Control.git

github p

run = True


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(input):
    input = list(input)
    output_list = []
    for i in input:
        i = (i + 3) % 10
        output_list.append(i)
    return output_list




while run:
    print_menu()
    menu_input = input("Please enter an option: ")
    if menu_input == 1:
        password_input = input("Please enter your password to encode: ")
        encoded_password = encode(password_input)
        print("Your password has been encoded and stored!")
    if menu_input == 2:
        decoded_password = decode(encoded_password)
        print("The encoded password is " + encoded_password +", and the original password is " + decoded_password + ".")
    if menu_input == 3:
        run = False
        exit()