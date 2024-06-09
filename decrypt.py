def decrypt(encrypted_text, shift_letter):
    decrypted_text = ""
    for char in encrypted_text:
        position = alphabet.index(char)
        new_index = (position - shift_letter) % 26
        new_char = alphabet[new_index]
        decrypted_text += new_char
    print(f"The decrypted text is {decrypted_text}")

if direction == "encode":
    encrypt(plain_text = text, shift_letter = shift)
elif direction == "decode":
    decrypt(encrypted_text = text, shift_letter = shift)


