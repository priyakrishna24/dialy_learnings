alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction=input("Type 'encode' to encrypt, type 'decode to decrypt:\n").lower()
# text=input("Type your message:\n").lower()
# shift=int(input("Type the shift number:\n"))

repetition=False
while not repetition:

    # direction=input("Type 'encode' to encrypt, type 'decode to decrypt:\n").lower()
    # text=input("Type your message:\n").lower()
    # shift=int(input("Type the shift number:\n"))

    def encrypt(original_text,shift_amount):
        text=''
        for letter in original_text:
            if letter in alphabet:
                shifted_position=(alphabet.index(letter)+shift_amount )% 26
                text+=alphabet[shifted_position]
            else:
                text+=letter
        return text

    def decrypt(original_text,shift_amount):
        text=''
        for letter in original_text:
            if letter in alphabet:
                shifted_position=(alphabet.index(letter)-shift_amount)%26
                text+=alphabet[shifted_position]
            else:
                text+=letter
        return text
    
    direction=input("Type 'encode' to encrypt, type 'decode to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    if direction=='encode':
        encrypted_message=encrypt(text,shift)
        print(f"Here's the encoded result: {encrypted_message}" )
    elif direction=='decode':
        decrypted_message=decrypt(text,shift)
        print(f"Here's the encoded result: {decrypted_message}")
    else:
        print('Your direction is not correct, check your direction')

    rep=input("Type 'yes' if you want to go again. Otherwise 'no'.")

    

    if rep!='yes':
        repetition=True
        print(f"That's it. Thank You!!!")
