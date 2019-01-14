filename = 'A history of postal agitation.txt'

try:
    with open(filename, encoding="utf8") as f:
        text = f.readlines()

except FileNotFoundError:
    print("Sorry, the file " + filename + " does not exist.")

else:
    count = 0
    search = 'agitation'
    for line in text:
        count += line.lower().count(search)
    print('Word ' + search + ' appears ' + str(count) + ' times.')