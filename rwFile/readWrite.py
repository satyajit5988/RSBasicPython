file = open('C:\\Users\\smore\\PycharmProjects\\BasicPython\\rwFile\\test.txt')
# Read all the contents of file
# Read n number of characters by passing parameter
# print(file.read())
# print(file.read(5))

# Read one single line at a time - readLine()

# print(file.readline())
# print(file.readline())

# print one line by line

# line = file.readline()
# while line != "":
#    print(line)
#    line = file.readline()

for line in file.readlines():
    print(line)

file.close()
