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
    
    
#The name of this function is called cipher, which includes two positional arguments and one keyword argument. Inside the function, we first create a list of all the letters, including lowercased and uppercased, in the alphabet and name that list "alphabet". Next, we create an empty list named "new_text" inside which we will store our output. 
