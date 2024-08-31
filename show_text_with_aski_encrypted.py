
def encrypt(text : str):

    encrypted_text = ''

    for char in text:

        char_aski = ord(char) * 21
        char_encrypted = chr(char_aski)
        encrypted_text += char_encrypted

    return encrypted_text



def decrypt(encrypted_text : str):

    decrypted_text = ''

    for char in encrypted_text:

        char_aski = ord(char) // 21 
        char_decrypted = chr(char_aski)
        decrypted_text += char_decrypted

    return decrypted_text



text = 'hello this is a homework for python plus'

enc_text = encrypt(text)

print("encrypted text: ",'\n',enc_text,'\n')


user_input = input('enter the algorithm: ')

if user_input.replace(' ', '') == '//21':
    print("\ndecrypted text: ",'\n',decrypt(enc_text),'\n')

else:
    print("Incorrect!!")
