def SimpleSymbols(str):
    chars = ['a', 'd', 'c', 'z']
    # code goes here
    for i in range(len(str)):
        if str[i] in chars:
            if str[i-1] == '+' and str[i+1] == '+':
                pass
            else:
                return False
    return True
    
# keep this function call here  
print(SimpleSymbols("+d+=3=+s+"))