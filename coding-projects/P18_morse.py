# POTD 18 skel
# Author: Mackenzie Gallovitch
# Date: 03 March 2026
# Description: Morse Code Translator
import sys

def get_dictionary(code_file):
    """ Generate a morse code dictionary from code_file. Each line of the file
    contains a single character, a space, then a sequence of . and - characters
    comprising the code for that character. The returned dicationary maps each
    character to its code. As a special case, not included in the input file,
    the space character (" ") should map to the empty string ("").
    Parameters: code_file is the name of a file in the current directory with the morse code mappings for upper case letters
    Returns: a dictionary with characters (letters in upper case) as keys and the morse code string as values
    """
    with open(code_file, "r") as f_in:
        morse_dict = {}
        
        for line in f_in:
            line = line.strip()
            chunk = line.split()
            char = chunk[0]
            code = chunk[1]
            
            morse_dict[char] = code
        morse_dict[" "] = ""
            
        return(morse_dict)
    

def reverse_dictionary(d):
    """ Build the reverse codebook for a given dictionary. Returns a new
    dictionary where each key is a value in d, and its value is the
    corresponding key in d. 
    Parameters: d is a dictionary
    Returns: a dictionary with keys and values reversed
    """
    rev_dict = {}
    
    for char in d:
        code = d[char]
        rev_dict[code] = char
    
    rev_dict[""] = " "
    
    return(rev_dict)
    
    

def translate_fwd(codebook, message):
    """ Translate from regular characters (A-Z, 0-9) to morse code using the
    given codebook, separating each code with a space. Unrecognized characters
    should be represented with a question mark (?). 
    Parameters: 
        codebook is a dictionary mapping characters (letters in upper case) to morse code
        message is a string of characters (letters in upper case)
    Returns: a string translated from characters to morse code
    """
    
    message = message.upper()
    translated = []
    
    for char in message:
        code = codebook.get(char, "?")
        translated.append(code)
    
    return(" ".join(translated))
       

def translate_rev(codebook, message):
    """ Translate from morse code characters back to regular characters using
    the given codebook whose keys are morse codes and values are characters.
    In the input message, the characters are separated by spaces, and words are
    separated by two spaces in a row. Unrecognized characters should be
    represented with a question mark (?).
    Parameters:
        codebook is a dictionary mapping morse code to characters (letters in upper case)
        message is a string of morse code
    Returns: a string translated from morse code to characters
    
    """
    translate = []
    message = message.split(" ")
    
    for code in message:
        char = codebook.get(code, "?")
        translate.append(char)
    
    return("".join(translate))


if __name__ == "__main__":
    
    filename = sys.argv[1]
    message = sys.argv[2]
    
    dictionary = get_dictionary(filename)
    rev_dictionary = reverse_dictionary(dictionary)
    
    if message[0] in ".-":
        result = translate_rev(rev_dictionary, message)
        
    else:
        result = translate_fwd(dictionary, message)

          
    print(result)