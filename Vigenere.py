# Vigenere Encryption function
def Encryption(plaintext, num_key):
    count = 0
    # Empty String
    ciphertext = ''
    for i in range(len(plaintext)):
        char0 = plaintext[i]
        char = char0.lower()
        # blank
        if char == " ":
            ciphertext += ' '
        # check for numbers and leave them that way
        elif char.isdigit():
            ciphertext += char
        # message Encryption
        elif char.isalpha():
            # Counter and list with positions
            if count < len(num_key):
                key1 = num_key[count]
                # Shifting letters (ASCII Table)
                ciphertext += chr((ord(char) + key1 - 97) % 26 + 97)
                # count ++ for shifting the list positions
                count += 1
            # start from the beginning of the list
            if count == len(num_key):
                count = 0

    return ciphertext


# Vigenere Decryption function
def Decryption(ciphertext, num_key):
    count = 0
    # Empty String
    plaintext = ''
    for i in range(len(ciphertext)):
        char0 = ciphertext[i]
        char = char0.lower()
        # blank
        if char == " ":
            plaintext += ' '
        # check for numbers and leave them that way
        elif char.isdigit():
            plaintext += char
        # message Decryption
        elif char.isalpha():
            # Counter and list with positions
            if count < len(num_key):
                key1 = num_key[count]
                # Shifting letters (ASCII Table)
                plaintext += chr((ord(char) - key1 - 97) % 26 + 97)
                # count ++ for shifting the list positions
                count += 1
            # start from the beginning of the list
            if count == len(num_key):
                count = 0
    return plaintext


# Intro!!
if __name__ == "__main__":
    print(50 * '*')
    print('#' + 10 * ' ' + 'Author : ShadowRoot18' + 17 * ' ' + '#')
    print('#' + 10 * ' ' + 'Algorithm : Vigenere ' + 17 * ' ' + '#')
    print('#' + 10 * ' ' + 'Category : Cryptography' + 15 * ' ' + '#')
    print(50 * '*' + '\n')
    num_key = []
    # Main Program
    while True:
        print('[*] Press 1 for Encryption \n[*] Press 0 for Decryption \n[*] Press 01 to exit.. ')
        choice = input('Insert Here : ')
        if choice.isdigit():
            if choice == '1':
                plaintext = input('Please insert the plaintext : ')
                # check if the key consists only of letters !
                while True:
                    key0 = input('Please insert the key : ')
                    if len(key0) <= len(plaintext):
                        if key0.isalpha():
                            key = key0.lower()
                            for i in range(len(key)):
                                key1 = key[i]
                                num_key.append(ord(key1) - 97)
                            break
                    else:
                        print('The length of the key must be lower or equal to the plainext ! \n')
                # output of encryption
                print('\n')
                print(50 * '*')
                print(f'[*] Ciphertext --> {Encryption(plaintext, num_key)}')
                print(50 * '*' + '\n')
            elif choice == '0':
                ciphertext = input('Please insert the ciphertext : ')
                # check if the key consists only of letters !
                while True:
                    key0 = input('Please insert the key : ')
                    if key0.isalpha():
                        key = key0.lower()
                        for i in range(len(key)):
                            key1 = key[i]
                            num_key.append(ord(key1) - 97)
                        break
                # output of Decryption
                print('\n')
                print(50 * '*')
                print(f'[*] Plaintext --> {Decryption(ciphertext, num_key)}')
                print(50 * '*' + '\n')
            # Just exit that sh#!@ xD
            elif choice == '01':
                print('Exiting..')
                break
            # Exception for users wrong input !
            else:
                print('Exception error .. \n'
                      'Please insert : 0|1|01')
