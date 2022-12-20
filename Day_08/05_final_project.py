#caesar-cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text,shift,direction):
    output_text = ''
    if direction=='decode':
        shift*=-1

    for char in text:
        if char in alphabet:
            output_text += alphabet[alphabet.index(char)+shift]
        else:
            output_text += char

    print(f"The {direction}d text is {output_text}")


should_continue = True
while(should_continue):
    direction = input("Type 'encode' to encript , type 'decode' to decrypt:\n" )
    text = input("Types your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%25      #%25 for large shift

    if direction == 'encode' or direction == 'decode':
        caeser(text=text,shift=shift,direction=direction)
    else:
        print("Wrong input!!!")
    
    i = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if i=="no":
        should_continue = False
        print("Goodbye!!!")
    