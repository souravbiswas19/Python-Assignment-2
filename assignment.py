def encryption(m, k):
    enc_msg=''
    for i in m:
        enc_msg=enc_msg+chr(ord(i)+k)
    return enc_msg

def decryption(m, k):
    dec_msg=''
    for i in m:
        dec_msg=dec_msg+chr(ord(i)-k)
    return dec_msg

msg = input('Enter the message:')
key = int(input('Enter the key (an integer):'))
mode = input('Choose mode (encrypt/decrypt):')

if mode == 'encrypt':
    print(encryption(msg, key))
elif mode == 'decrypt':
    print(decryption(msg, key))
else:
    print('Invalid mode')