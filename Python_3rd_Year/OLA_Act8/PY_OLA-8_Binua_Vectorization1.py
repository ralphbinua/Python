print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

# vectorization without ufunc

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
 z.append(i + j)
print(z)