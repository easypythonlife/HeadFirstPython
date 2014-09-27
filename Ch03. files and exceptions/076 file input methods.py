# import os
# os.getcwd()
# os.chdir('.')

data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')

data.seek(0)
for each_line in data:
    print(each_line, end='')
data.close()