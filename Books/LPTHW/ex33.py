numbers = []

# def while_list(length, step=1):
#     i = 0
#     while i < length:
#         print(f"At the top i is {i}")
#         numbers.append(i)
#         i = i + step
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")


def for_list(length, step=1):
    for i in range(0, length, step):
        print(f"At the top i is {i}")
        numbers.append(i)
        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

# while_list(length=int(input('Enter a length of a list: ')), \
#              step=int(input('Enter a step: ')))

for_list(length=int(input('Enter a length of a list: ')), \
           step=int(input('Enter a step: ')))


print("The numbers: ")
for num in numbers:
    print(num)
