# try, catch

try:
    with open('C:\\Users\\smore\\PycharmProjects\\BasicPython\\rwFile\\test.txt', 'r') as reader:
        reader.read()
except:
    print("File Not Found")

finally:
    print("Final Result")


try:
    with open('C:\\Users\\smore\\PycharmProjects\\BasicPython\\rwFile\\file.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Final")
