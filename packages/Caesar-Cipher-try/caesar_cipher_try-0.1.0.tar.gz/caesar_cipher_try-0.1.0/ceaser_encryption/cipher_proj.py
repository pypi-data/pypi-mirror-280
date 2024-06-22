
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:32:52 2024

@author: abdom
"""
import re



class CaeserCipher :
    global encryption_key 
    encryption_key = {
    'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 
    'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 
    'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 
    'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 
    'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 
    'Z': 'C' ,' ': ' '}

    global decryption_key 
    decryption_key = {
    'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 
    'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 
    'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O', 
    'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 
    'X': 'U', 'Y': 'V', 'Z': 'W', 'A': 'X', 'B': 'Y', 
    'C': 'Z', ' ': ' '}
    
    def __init__(self, encryption_key=encryption_key , decryption_key=decryption_key ):
        self.encryption_key = encryption_key
        self.decryption_key = decryption_key
    
    def encrypt_string(self , decr_mess : str()) :
        
        self.enc_str = str()
        
        for x in decr_mess :
            for y in encryption_key.keys():
                if y == x.capitalize() :
                    self.enc_str+= encryption_key[y]
        return self.enc_str


    def decrept_string(self , enc_mess : str()) :
        
        self.dec_str = str()
        
        for x in enc_mess :
            for y in encryption_key.keys():
                if y == x.capitalize():
                    self.dec_str += decryption_key[y]
        return self.dec_str


    def check_input(self ,string):
        # Check if the string contains only alphabets and spaces
        if re.match("^[A-Za-z\s]*$", string):
            print("Input is valid.")
        else:
            raise ValueError("Invalid input: Only alphabets and spaces are allowed.")

    def get_cipher (self ,text : str() , key = None , encrypt = True ):
        if encrypt == True :
            if key is not None :            
                self.encryption_key= key
                return self.encrypt_string(text)
            else :
                self.encryption_key= encryption_key
                return self.encrypt_string(text)
        else :
            if key is not None :            
                self.decryption_key= key
                return self.decrept_string(text)
            else :
                self.decryption_key= encryption_key
                return self.decrept_string(text)

'''message= "ahmed want to play football"
first_cipher = CaeserCipher()


enc_messs = first_cipher.get_cipher(text =message,encrypt=True)

print(enc_messs)
dex_mess =first_cipher.get_cipher(text =enc_messs,encrypt=False)
print(dex_mess)'''