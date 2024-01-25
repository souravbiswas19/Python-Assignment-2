def encryption(m, k): #function to encrypt the message
    enc_msg='' #variable that will store the encrypted message
    for i in m: #iterating through the string
        enc_msg=enc_msg+chr(ord(i)+k) #encrypting by subtracting the key value to the given message
        #ord() function converts string characters to ASCII values and chr() returns the character corresponding to the ASCII value
    return enc_msg

def decryption(m, k): #function to decrypt the message
    dec_msg='' #variable that will store the decrypted message
    for i in m: #iterating through the string
        dec_msg=dec_msg+chr(ord(i)-k) #decrypting by subtracting the key value from the encrypted message
    return dec_msg

msg = input('Enter the message: ') #accepting the message
key = int(input('Enter the key (an integer): ')) #accepting the key
mode = input('Choose mode (encrypt/decrypt): ') #accepting the mode

#conditional statements for mode selection
if mode == 'encrypt': 
    print('Encrypted message: ',encryption(msg, key)) #print the encrypted message
elif mode == 'decrypt':
    print('Decrypted message: ',decryption(msg, key)) #print the decrypted message
else:
    print('Invalid mode') #incase of any other mode it will be declared as invalid