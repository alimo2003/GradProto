import mysql.connector
import string

def Encrypt():
    print("----- Encryption ------")    
    plain_text = input("Enter Your Message to encrypt: ")
    idkey = input("Enter the key ID you are using to encrypt: ")

    # Creating connection object
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2003199_Ali",
        database="CyberZ"
    )
    mycursor = mydb.cursor()

    # Correct SQL query and value binding
    sql = "SELECT keycipher FROM ENC WHERE Id = %s"
    val = (idkey, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Remove spaces from cipherkey and convert to list
        cipherkey = list(result[0].replace(" ", ""))  
        cipherkey.append(" ")
        print(f"Cipher Key: {''.join(cipherkey)}")
        
        # Create reference alphabet as a list
        reference_alphabet = list(string.ascii_letters + string.digits + string.punctuation + ' ')
        print(f"Reference Alphabet: {''.join(reference_alphabet)}")

        # Print lengths for debugging
        print(f"Length of Cipher Key: {len(cipherkey)}")
        print(f"Length of Reference Alphabet: {len(reference_alphabet)}")

        if len(cipherkey) != len(reference_alphabet):
            print("Error: Cipher key length does not match the reference alphabet length!")
            return

        cipher_text = ""  # Initialize encrypted message

        for letter in plain_text:
            # Check if letter is in reference alphabet
            if letter in reference_alphabet:
                index = reference_alphabet.index(letter)
                cipher_text += cipherkey[index]
            else:
                cipher_text += letter  # Directly append characters not in the reference alphabet

        print(f"Encrypted Message: {cipher_text}")

    else:
        print("Key ID not found.")

    # Closing the connection
    mydb.close()

    Menu()

def Menu():
    X = input("1-Encryption \n2-Decryption \n3-Exit \nWhich Operation do you need?\n")
    if X == '1':
        Encrypt()
    else:
        exit()

if __name__ == "__main__":
    Menu()
