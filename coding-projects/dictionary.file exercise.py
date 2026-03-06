#Author: Mackenzie Gallovitch
#Date: 6 March 2026
#Description: Some fun, random coding exercising my abilities to read/write files and create dictionaries and retrieve their values.

def make_copy_file(file_name):
    """Copies a file's data into another copy created in the function. """
    
    copy = "copy.txt"
    
    with open(file_name, "r") as f_in:
        with open(copy, "w") as f_out:
            for line in f_in:
                f_out.write(line)
                
    return(copy)
                
def make_dictionary(file_name):
    """Makes a dictionary out of the file. """
    
    my_dict = {}
    
    with open(file_name, "r") as f:
        next(f)
        
        for line in f:
            if ":" in line:
                line.strip()
                key, value = line.split(":", 1)
                
                my_dict[key.strip()] = value.strip()
                
    return my_dict

def make_type_dictionary(dictionary):
    """Assigns media types to fictional characters.
    Precondition: dictionary keys that are even result in book characters
    while odd keys result in anime characters. """
    type_dict = {}
    
    for key in dictionary:
        i = int(key)
        if i % 2 == 0:
            i = str(i)
            name = dictionary[i]
            type_dict[name] = "Book Character"
        else:
            i = str(i)
            name = dictionary[i]
            type_dict[name] = "Anime Character"
        
    return type_dict     
            
            
if __name__ == "__main__":
    
    import_file = "List of Men I can Tolerate.txt"
    
    copy_file = make_copy_file(import_file)
    
    new_dict = make_dictionary(copy_file)
    
    typ_dict = make_type_dictionary(new_dict)
    
    for i in range(1, len(new_dict) + 1):
        i = str(i)
        print(new_dict.get(i))
        names = new_dict.get(i)
        
    print("\n")
    
    for key in typ_dict:
        print(typ_dict.get(key))
        types = typ_dict.get(key)
        
    print("\n")
    
    for name in typ_dict:
        character_type = typ_dict[name]
        print(name, ": ", character_type, sep="")
    
    
    
    
    