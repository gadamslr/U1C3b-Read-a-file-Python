def decrypt(encrypted):
    
    decrypted = ""
    
    for letter in encrypted:
        
        if ord(letter) >= 97 and ord(letter) <= 122:
            decrypted = decrypted + chr(ord(letter) - 2)
        else:
            decrypted = decrypted + letter

    return decrypted


encryptedMessage ="ftqigt ecuvng"

calc(encryptedMessage)

returnedValue = decrypt(encryptedMessage)

print(returnedValue)

