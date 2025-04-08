string = input("Please enter a word: ")
char = input("Please eneter your own character: ")
i = 0
count = 0

while (i < len(string)):

    if(string[i] == char):
        count = count + 1
    i = i + 1

print("the Total Number Of Times ", char,"has Occured = ", count)
