a = 0.5
b = "Howdy!"
c = True

print([type(var) for var in [a, b, c]])
types = [type(var) for var in [a, b, c]]

print(type(a))
print(type(b))
print(type(c))
print(types)