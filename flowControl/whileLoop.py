it = 5

while it > 1:
    print(it)
    it = it - 1

print("While loop execution is done")

print("#############################")


it = 10

while it > 0:
    if it == 9:
        it = it - 1
        continue
    print(it)
    it = it - 1

print("While loop execution is done")