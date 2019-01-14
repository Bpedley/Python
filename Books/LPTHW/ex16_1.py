fliename = 'ex16.txt'

file = open(fliename)
print(f"Here's your file {fliename}:")
print(file.read())

file.close()
