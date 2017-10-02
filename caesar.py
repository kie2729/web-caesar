
def encrypt(text, rot):
    new_message = ''
    for char in text:
        new_char = rotate_character(char, rot)
        new_message = new_message + new_char

    return new_message

def alphabet_position(letter):
    """return the index of a letter in teh alphabet"""

    alphabet='abcdefghijklmnopqrstuvwxyz'
    ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if letter.isupper() == True:
        for x in ALPHABET:
            if letter == x:
                position = ALPHABET.index(x)
        return position

    else:
        for x in alphabet:
            if letter == x:
                position = alphabet.index(x)
        return position

def rotate_character(char, rot):
    """return a character 'rot' farther in the alphabet"""
    if char.isalpha() == False:
        return char

    else:
    
        original_pos = alphabet_position(char)
        new_pos = original_pos + rot

        if new_pos >=26:
            new_pos = new_pos % 26

        alphabet='abcdefghijklmnopqrstuvwxyz'
        ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        
        if char.isupper() == True:
            new_char = ALPHABET[new_pos]
        else:
            new_char = alphabet[new_pos]
            
        return new_char

        

def main():
    text = input('Type a message:')
    rot = int(input('Rotate by:'))

    print(encrypt(text,rot))

if __name__ == "__main__":
    main()