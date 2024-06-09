
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# A Function called 'encrypt' takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_letter):
    input(f"The text you entered is {text} and the shift is {shift}")
    
    
#Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    
    encrypted_text = ""
    for char in plain_text:
         if char in alphabet:
             position = alphabet.index(char)
             new_index  = (position + shift_letter) % 26
             new_char = alphabet[new_index]
             encrypted_text += new_char
    print(f"The encrypted text is {encrypted_text}")
         
    
#Check the result of encrypt function and pass in the user inputs.
encrypt(plain_text = text, shift_letter = shift)
