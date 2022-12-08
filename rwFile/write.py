# Read the file and store in list
# Reverse the lines
# Write to the file

with open('C:\\Users\\smore\\PycharmProjects\\BasicPython\\rwFile\\test.txt', 'r') as reader:
    content = reader.readlines()
    rc = reversed(content)
    with open('C:\\Users\\smore\\PycharmProjects\\BasicPython\\rwFile\\test.txt', 'w') as writer:
        for line in rc:
            writer.write(line)
