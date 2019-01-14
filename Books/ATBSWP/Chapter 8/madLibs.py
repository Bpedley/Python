import re

madLibs = open('libs.txt')
text = madLibs.read()
madLibs.close()

libsRegex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')
for i in libsRegex.findall(text):
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            inp_text = input('Enter the substitute for %s: ' %j)
            text = reg.sub(inp_text, text, 1)

print(text)

madLibs = open('libs1.txt', 'w')
madLibs.write(text)
madLibs.close()
