import mysql.connector
import random
import string

keyL2=[]
keyL1=[]

all_chars = string.ascii_letters + string.digits + string.punctuation + ' '
keyL0 = list(all_chars)
keyL1 = keyL0.copy()
random.shuffle(keyL1)
id= random.randint(100000, 999999)

# Convert the list to a string
my_string = ' '.join(keyL1)

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2003199_Ali",
    database = "CyberZ"
)
mycursor = mydb.cursor()
sql = "INSERT INTO ENC (Id, keycipher) VALUES (%s, %s)"
val = (id , my_string)
mycursor.execute(sql, val)
mydb.commit()
# disconnecting from server
mydb.close()

print("Key Successfully made:", id)

