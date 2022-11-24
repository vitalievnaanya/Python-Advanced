def write_to_files(path_file, mode, text):
    file = open(path_file, mode)
    file.write(text)
    file.close()

write_to_files('number.txt', 'w', '''1
2
3
4
5
6
''')

write_to_files('number.txt', 'a', '''NEW 
TEXT''')