import random


print("対象文字：")

a = ["A", "B", "C", "D", "E", "F", "G", 
"H", "I", "J", "K", "L", "M", "N", 
"O", "P", "Q", 
"R", "S", "T", 
"U", "V", "W", "X", "Y", "Z"]



b = random.randrange(0,25)
print(b)
print(a[b]+"\r\n")


li1 = []
li1 = random.sample(a, 10)

# print(li1)
print("")

li2 = []
li2 = random.sample(li1, 2)

# print(li1)
# print(li2)

for i in range(0, 9):
    print(li1[i] + " ", end="")
    

    # if (a[c] in li1) :
    #     i -= 1
    #     continue

    # li1.append(a[c])
    # print(li1[i])

print("\r\n")
print("欠陥文字：")


for i in range(0, 2):
    print(li2[i] + " ", end="")


li1.remove(li2)

print(li1)



