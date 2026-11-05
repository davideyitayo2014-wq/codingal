string = input("Please enter your ownn word : ")

char = input("Please enter your own Character : ")
i = 0
count = 0

while(i < len(string)):

    if(string[i] == char):
        count = count + i
    i = i + 1

    print("The total number of times ", char, " has Occured = ", count)