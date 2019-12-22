"""
Для заданого списку чисел, вивести суму усіх парних та непарних елементів цього списку.
"""


lst = [1, 3, 4, 7, 9, 4, 8, 12, 14, 5]
a = len(lst)
i = 0
resultP = int()
resultNP = int()
while i <= a:
    if lst[i] % 2 == 0:
        resultP += lst[i]
    else:
        resultNP += lst[i]
    i += 1
print("Сума парних: " + str(resultP))
print("Сума непарних: " + str(resultNP))