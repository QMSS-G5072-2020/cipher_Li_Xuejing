def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
    
    
'''
 The name of this function is called cipher, which includes two positional arguments and one keyword argument. Inside the function, we first create a list of all the letters in the alphabet, including lowercased and uppercased, and name that list "alphabet". Next, we create an empty list named "new_text" inside which we will store our output. The function says for every letter in our input for the text argument, we will first find if the letter is in the list alphabet. If it's not in the alphabet list, we will return the output exactly as the imput. If it's in the alphabet list, we want to return an output where the lens doesn't change but the position of each letter either shifts to the right or to the left depends on whether the encrypt argument is true or not.
 
Encrypting Example
------------------
>>> Encrypted = cipher('bird',5,encrypt = True)
>>> 'gnwi'

Decrypting Example
------------------
>>> Decrypting = cipher(Encrypted, 5, encrypted = False)
>>> 'bird'
'''
