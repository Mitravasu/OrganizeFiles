def pythonPath(path: str):
    new_path = ""
    for letter in path:
        new_path += letter
        if(letter == '\\'):
            new_path += '\\'
    return new_path