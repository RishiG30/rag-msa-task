# to find the average of list of numbers

entry = list(map(int, input("Enter the elements present in the list: ").split()))

positive_integer = []

l1 = entry
for each_number in l1:
    if each_number >= 0:
        positive_integer.append(each_number)

average = sum(positive_integer) / len(positive_integer)

print(f"{average} is the average of the given positive numbers.")



