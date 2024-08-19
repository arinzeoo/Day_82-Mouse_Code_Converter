# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '+'}


# Function to convert
def listToString(list):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(list))


def encrypt_message():
    # Prompt user for message to encrypt
    user_input = input('Enter message to encrypt: ').upper()
    # Convert User input to Morse Code
    encrypted_list = [MORSE_CODE_DICT[letter] for letter in user_input]
    # convert list to string
    morse_message = listToString(encrypted_list)
    # return string
    return morse_message


def decrypt_message():
    # Prompt user for morse code to decrypt
    user_input = input('Enter message to decrypt: ')
    # Convert the morse code to list
    input_to_list = user_input.split(' ')
    message = ''
    for item in input_to_list:
        s = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(item)]
        message += s
    return message


app_exit = False
# Create a while loop
while not app_exit:
    # App menu
    menu = input("APP MENU: "
                 "\n 1. To encrypt a message type '1'"
                 "\n 2. To decrypt a message type '2'"
                 "\n 3. Type 'Exit' to end the app \n >>>")

    if menu == '1':
        print(encrypt_message())
    elif menu == '2':
        print(decrypt_message())
    elif menu == 'Exit':
        app_exit = True
    else:
        print('Input a valid option!')




