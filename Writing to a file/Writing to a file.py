print("Creating a text file with write method")
textfile=open("N:\KS4\Computer Science\Python\Writing to a file\write_it.txt", "a")
              
textfile.write("line\n")
textfile.write("hello\n")
textfile.write("writing the file")
textfile.close()


textfile=open("N:\KS4\Computer Science\Python\Writing to a file\write_it.txt", "r")
print(textfile.read())
textfile.close()
