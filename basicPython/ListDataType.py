values = [1, 2, "Rahul", 0.25, 5]

print(values[0])
print(values[-1])
print(values[1:5])

values.insert(3, "More")
print(values[0:6])

values.remove("Rahul")
print(values[0:5])

values.append("End")
print(values)

values[1] = "ADAM"
print(values)

del values[0]
print(values)