import subprocess

'''
calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calcProc.poll() == None)
print(calcProc.wait())
print(calcProc.poll())
subprocess.Popen(['C:\\Windows\\notepad.exe', 'D:\\hello.txt'])
subprocess.Popen(['C:\\Users\\kuchi\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe', 'calcProd.py'])
'''

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()

subprocess.Popen(['start', 'hello.txt'], shell=True)