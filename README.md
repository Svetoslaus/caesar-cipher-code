#encrypt.py
----------------
The program is about implementing a Caesar cipher, a basic encryption technique used to encode a message by shifting each letter by a fixed number of positions in the alphabet. Here's a breakdown of what the program does:

User Interaction:

The program asks the user to input whether they want to encode or decode a message.
It then prompts the user to enter the message they want to process.
Finally, the user is asked to provide a shift number, which determines how many positions each letter in the message will be shifted.
Encrypt Function:

The program defines a function called encrypt that takes the message and the shift number as inputs.
Inside this function, it processes each letter of the message:
If the letter is in the alphabet, it finds the letter's position in the alphabet.
It calculates the new position by adding the shift number to the current position, using modulo 26 to wrap around the alphabet if necessary.
It then appends the letter at the new position to an encrypted message string.
After processing all the letters, it prints the encrypted message.

Execution:

The program calls the encrypt function with the user-provided message and shift number to produce and display the encrypted message.
