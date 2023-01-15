def max_pair_wise_product(digitList):
    index1 = 0
    for i in range(1,len(digitList)):
        if digitList[i] > digitList[index1]:
            index1 = i

    index2 = 0
    for j in range(1, len(digitList)):
        if digitList[j] != digitList[index1] and digitList[j] > digitList[index2]:
            index2 = j
    print(f"Max pair product value is {digitList[index1] * digitList[index2]}")

a = int(input("Enter the numbers of digit: "))
b = input().split()
digitList = []

for i in range(len(b)):
    digitList.append(int(b[i]))
max_pair_wise_product(digitList)