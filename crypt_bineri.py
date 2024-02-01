print("welcome to bineri to text and text to bineri")
ask1 = input("wold you like to crypt or dicrypt? c/d ")

def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)
def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
if ask1 == "c":
 text = input("plz enter a text ")
 print(f"The binary representation of '{text}' is {text_to_binary(text)}")

elif ask1 == "d":
   binary = input("plz entr bineri.")
   print(f"The text representation of '{binary}' is '{binary_to_text(binary.replace(' ', ''))}'")



