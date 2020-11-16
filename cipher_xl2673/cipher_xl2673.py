def cipher(text, shift, encrypt=True):
    '''
    Cipher code that encrypt and decrypt texts.
    
    Parameters
    ----------
    text: str
        The text string to be encrypted or decrypted
    shift: int
        An interger number upon which the text will shift along the alphabet list
    encrypt: bool
        A boolean value. If it's True, we would encrypt the text; if it's False, we would decrypt the text
    
    Returns
    -------
    Str
    Either an encrypted or decrypted text
    
 
    Example
    ------------------
    from cipher_xl2673 import cipher_xl2673
    >>> Encrypted = cipher('bird',5,encrypt = True)
    >>> 'gnwi'

    >>> Decrypted = cipher(Encrypted, 5, encrypted = False)
    >>> 'bird'
    '''

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
    
    
