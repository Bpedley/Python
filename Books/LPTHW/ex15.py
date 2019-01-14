from sys import argv

script, filename = argv                 # using argv to take a file name
                                        # from command-line                             
txt = open(filename)                    # Open a file in memory
print(f"Here's your file {filename}:")  # Print name of file
print(txt.read())                       # Print content of the file

txt.close()                             # Closing a file
