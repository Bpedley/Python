import zipfile, os

os.chdir('D:\\Python\\Books\\Automate the boring stuff with python') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.extractall()
exampleZip.extractall('D:\\delicious')
exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'D:\\some\\new\\folders')
exampleZip.close()

newZip = zipfile.ZipFile('New.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
