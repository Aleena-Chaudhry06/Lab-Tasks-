def remove_punctuations(input_string):
    result = ""
    
    punctuations = ".,!?;:'\"()[]{}<>-_=+@#$%^&*`~\\/|"
    for char in input_string:
        if char not in punctuations:
            result += char
    return result

string = input("Enter a string: ")
cleaned_string = remove_punctuations(string)
print("String without punctuations:", cleaned_string)
