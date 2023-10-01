logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
should_continue=True
def caeser(start_text,shift_amount,cipher_direction):
  end_text=""
  if cipher_direction=="decode":
      shift_amount*=-1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char) 
      new_position = position+shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {direction}d result: {end_text}")
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26



  caeser(start_text=text,shift_amount=shift,cipher_direction=direction)
  result=input("Type 'yes' if you want to go again.Otherwise type 'no'.")
  if result=="no":
    should_continue=False
    print("Goodbye")
def encrypt(plain_text,shift_amount):
  cipher_text=""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position+shift
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")
if direction=="encode":
  encrypt(text,shift)  

      
  for letter in start_text:
    position=alphabet.index(letter)
    new_position=position + shift_amount
    cipher_text+=alphabet[new_position]
  print(f"The encoded text is {cipher_text}")
  
def decrypt(cipher_text,shift_amount):
  decipher_text=""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position-shift
    new_letter = alphabet[new_position]
    decipher_text += new_letter
  print(f"The decoded text is {decipher_text}") 
if direction=="decode":
  decrypt(cipher_text,shift) 
    
