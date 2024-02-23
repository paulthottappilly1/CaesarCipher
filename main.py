alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function that takes in the text to be encrypted by a shift number
def CaesarCipher(text, shift):
    new_word = ""

    #if statement that shifts the messages to be encoded/decoded and prints it out
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            letter_index = letter_index + shift
            new_word += alphabet[letter_index % len(alphabet)]
        else:
            new_word += char

    print(f"The {direction}d text is '{new_word}'\n")

from art import logo
print(logo)

#while loop that'll keep iterating until the user inputs encode or decrypt
continue_cipher = True
while continue_cipher:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction not in ("encode", "decode"):
            print("Invalid input, please enter a valid input!")
            continue
        else:
            break
    #prompts the user to input the message to be encoded/decoded and the shift number
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #calls the cipher function
    CaesarCipher(text, shift)

    #checks to see if the user would like to keep running the program
    restart = input("If you'd like to keep encrypting/decrypting messages, type 'yes'. If you'd like this program to end, type 'no'.\n")
    if restart.lower() == "no":
        continue_cipher = False
        print("Goodbye, have a wonderful day!")
        