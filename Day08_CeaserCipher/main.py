import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):

  text_array = list(text)

  updated_array = []
  for i in range(0, len(text_array)):
    shifted_index = alphabet.index(text_array[i]) + shift
    updated_array.append(alphabet[shifted_index]) 

  updated_text = ''
  for i in updated_array:
    updated_text += i
  
  print(f"Your encrypted message is {updated_text}")

def decryption(text, shift):

    text_array = list(text)

    updated_array = []
    for i in range(0, len(text_array)):
      shifted_index = alphabet.index(text_array[i]) - shift
      updated_array.append(alphabet[shifted_index]) 

    updated_text = ''
    for i in updated_array:
      updated_text += i
    
    print(f"Your decrypted message is {updated_text}")



print(art.logo)

while True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if(direction == 'encode'):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
    answer = input('do you want try again? yes/no ').lower()
    if  ( answer == 'no'):
      break
  elif(direction == 'decode'):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decryption(text, shift)
    answer = input('do you want try again? yes/no ').lower()
    if(answer == 'no'):
      break
  else:
    print("Wrong value.\n")


