from art import logo
print(logo)




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def encrypt(original_text, shift_amount):
    encrypt_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypt_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            encrypt_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {encrypt_text}")






def decrypt(original_text, shift_amount):
    decrypt_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypt_text += letter
        else:

            shifted_position = alphabet.index(letter) - shift_amount
            decrypt_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {decrypt_text}")

def caeser(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        encrypt(original_text=text, shift_amount=shift)
    else:
        decrypt(original_text=text, shift_amount=shift)




caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")




