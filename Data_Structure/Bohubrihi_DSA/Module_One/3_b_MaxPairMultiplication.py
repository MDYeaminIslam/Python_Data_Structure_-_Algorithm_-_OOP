def max_pair_wise_product(digitList):
    max_pair_product = 0
    for i in range(len(digitList)):
        for j in range(i+1, len(digitList)):

            max_pair_product = max(max_pair_product, digitList[i] * digitList[j])

    print(f"Max pair value is {max_pair_product}.")

a = int(input("Enter the numbers of digit: "))
b = input().split()
digitList = []

for i in range(len(b)):
    digitList.append(int(b[i]))
max_pair_wise_product(digitList)
