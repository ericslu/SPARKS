LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translate(k, message, mode):
  translated = ""
  keyIndex = 0
  key = k.upper()

  # Iterate through word character by character
  for char in message:
    ASCIIndex = LETTERS.find(char.upper())
    if (ASCIIndex != -1):
      ASCIIndex += LETTERS.find(key[keyIndex])
      ASCIIndex %= len(LETTERS)
    if (char.isupper()):
      translated += LETTERS[ASCIIndex]
    else:
      translated += (LETTERS[ASCIIndex]).lower()

    keyIndex += 1
    if (keyIndex == len(key)):
      keyIndex = 0



# Main
"""
msg = input('Enter the message you want to encrypt: ')
key = input('Enter your key: ')
mode = input('Return 1 for encrypt, Return 2 for decrypt: ')

if (int(mode) == 1):
  translate(key, msg, 'encrypt')
elif (int(mode) == 2):
  translate(key, msg, 'decrypt')
"""
