def cats_dogs(filename):
    """Prints content of files."""
    try:
        with open(filename) as f:
            text = f.readlines()

    except:
        pass

    else:
        print('File with name ' + filename + ':')
        for line in text:
            print(line.rstrip())


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    cats_dogs(filename)