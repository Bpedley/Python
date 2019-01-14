filename = 'ex15_sample.txt'

file = open(filename)
print(f"Here's your file {filename}:")
print(file.read())

file.close()
