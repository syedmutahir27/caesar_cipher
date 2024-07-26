import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Caesar Function
def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
         position = alphabet.index(char)
          #accounts for wrap around from Z to A 
         new_position = (shift_amount + position)%26

         end_text += alphabet[new_position] 
        else:
            end_text += char
            

    print(f"your {cipher_direction} text is {end_text}")

#direction for choosing encryption/decryption
should_countinue = ''
while should_countinue != 'no':
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    should_countinue = input("Type 'yes' to go again . Otherwise  type 'no'\n").lower()
print("Goodbye!")