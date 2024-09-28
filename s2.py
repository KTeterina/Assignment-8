obj = ["element", 2, 3.5, 4, 5>6, "text"]

n_string = 0

for i in obj:
    if isinstance(i, str):
        n_string += 1

print("Number of string elements is ", n_string)