# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print ("\nThe new created array is : ", end = "")
for i in range (0, 3):
    print (a[i], end = "")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print ("\nThe new created array is : ", end = "")
for i in range (0, 3):
    print (b[i], end = "")

a.insert(1, 4)

print ("\nArray after insertion : ", end = "")
for i in (a):
    print (i, end = "")
print()

# adding an element using append()
b.append(4.4)

print ("\nArray after insertion : ", end = "")
for i in (b):
    print (i, end = "")
print()

print("Access element is: ", a[0])
print("Access element is: ", b[2])