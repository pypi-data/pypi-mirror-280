from Crypto.Cipher import AES
import base64
import os
from Crypto import Random
import hashlib
from Crypto.Hash import SHA256
from pbkdf2 import PBKDF2

import binascii
from io import StringIO
import base64
from AESHelper2.PKCS7Encoder import PKCS7Encoder

class AESHandler(object):
    # the block size for the cipher object; must be 16, 24, or 32 for AES
    BLOCK_SIZE = 32
    CipherMode = AES.MODE_CBC
    iv = b'@1B2c3D4e5F6g7H8'
    password = 'AERT99HY'
    salt = 's@1tMovis'
    iterations = 2
    derived_key = PBKDF2(password, salt, iterations).read(BLOCK_SIZE) # 256-bit key
    encoder = PKCS7Encoder()
    
    def Encrypt(self, plainText):
        cipher = AES.new(self.derived_key, self.CipherMode, self.iv)
        #padd the plain text
        pad_text = self.encoder.encode(plainText)
        #encrypt the padded text
        cipherText = cipher.encrypt(pad_text)
        #base64encode the cipher text
        b64enc_cipherText = base64.b64encode(cipherText)
        return b64enc_cipherText
        
    def Decrypt(self, cipherText):
        cipher = AES.new(self.derived_key, self.CipherMode, self.iv)
        b64dec_cipherText = base64.b64decode(cipherText)
        #base64decode the cipher text)
        decipher_text = cipher.decrypt(b64dec_cipherText)
        decoded_text = self.encoder.decode(decipher_text.decode("utf-8"))
        return decoded_text