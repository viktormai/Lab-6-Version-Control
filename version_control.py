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

def decode(password):
    password = encoder(password)
    pass_list: list[password]
    for i in password:
        j = int(i)
        if j > 2:
            k = j - 3
            print(k, end="")
        if j < 3:
            if j == 0:
                print("7", end="")
            if j == 1:
                print("8", end="")
            if j == 2:
                print("9", end="")
    return

def main():
    while True:
        print("Menu")
        print("-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        if option == 2:
            print("The encoder function is ", end="")
            print(encoder(password), end='')
            print(" and the original password is ", end='')
            decode(password)
        if option == 3:
            break


if __name__ == '__main__':
    main()
