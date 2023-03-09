def make_list(password):
    list1 = []
    list1[:0] = password
    password = list1
    return password


def encoder(password):
    table = {0: '3', 1: '4', 2: '5', 3: '6', 4: '7',
             5: '8', 6: '9', 7: '0', 8: '1', 9: '2'}
    encoded = ''
    password = make_list(password)
    for i in range(0, len(password)):
        password[i] = int(password[i])

    for num in password:
        encoded = encoded+table[num]
    return encoded


def main():
    while True:
        print("Menu")
        print("-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        # add decoder part here
        if option == 3:
            break


if __name__ == '__main__':
    main()
