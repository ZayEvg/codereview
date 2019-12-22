"""
Користувач вводить текст. Вивести усі слова цього тексту,що містить велику букву, у вигляді списку.
"""


text = str(input("Введіть текст: "))
lst = []
for count in range(0, len(text) + 1):
    if text[count].isupper():
        count2 = count + 1
        while text[count2] != " ":
            lst += text[count2]
            count2 += 1
