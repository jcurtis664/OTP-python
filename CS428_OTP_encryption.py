# -*- coding: utf-8 -*-
"""
Jared Curtis
CS 428
04/26/2021

OTP Encryption
"""

import os
import base64

'''FUNCTION THAT CONVERTS A BINARY STRING INTO ASCII STRING'''
def binary_string_to_ascii(string):
    result = int(string, 2)                             #converts string into binary int
    num_of_bytes = result.bit_length() + 7 // 8         #number of bytes in binary int
    
    result = result.to_bytes(num_of_bytes, 'big')       #converts result into bytes
    result = result.decode()                            #converts bytes into ascii
    
    return result[len(result) - int(len(string) / 8):]  #removes extra spaces


'''FUNCTION THAT USES CRYPTOGRAPHICALLY-SAFE RANDOM GENERATION TO CREATE KEY'''
def create_key(string):
    key = base64.b64encode(os.urandom(len(string)))     #creates string of ascii bytes
    return key


'''FUNCTION THAT ENCRYPTS A DESIRED ASCII STRING'''
def encrypt_string(string, key):
    binary_string = ''.join(format(ord(byte), '08b') for byte in string)    #converts string into binary
    binary_key = ''.join(format(ord(byte), '08b') for byte in str(key))     #converts key into binary
    
    binary_key = binary_key[:len(binary_string)]                            #trims excess key length
    
    print('Bit length of string = ', len(binary_string))
    print('Bit length of key = ', len(binary_key))
    
    encrypted_result = ''.join(str(int(binary_string[i])^int(binary_key[i])) for i in range(len(binary_string)))  #XORs string and key  
    return encrypted_result


'''FUNCTION THAT DECRYPTS A DESIRED BINARY STRING'''
def decrypt_string(enc_string, key):
    binary_key = ''.join(format(ord(byte), '08b') for byte in str(key))     #converts key into binary
    
    binary_key = binary_key[:len(enc_string)]                               #trims excess key length
    
    decrypted_result = ''.join(str(int(enc_string[i])^int(binary_key[i])) for i in range(len(enc_string)))  #XORs string and key
    decrypted_result = binary_string_to_ascii(decrypted_result)             #converts result to ASCII
    return decrypted_result


print('-============- ONE TIME PAD ENCRYPTION -============-')
test_str = input("Enter string to be encrypted : ")
test_key = create_key(test_str)
print()

encrypted_result = encrypt_string(test_str, test_key)
decrypted_result = decrypt_string(encrypted_result, test_key)

print()
print('Binary encryption of string : ', encrypted_result)
print()
print('ASCII encryption of string : ', binary_string_to_ascii(encrypted_result))
print()
print('ASCII decryption of string : ', decrypted_result)