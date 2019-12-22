"""
Використовуючи регулярні вирази, для поданого нижче тексту замініть кожне число на його шіснадцяткове представлення. Виведіть результат.
"""


def validator(pattern, prompt):
    txt = input(prompt)
    while not bool(pattern.findall(txt)):
        txt = input(prompt)
    return txt


def change_text(pattern, promt):
    txt = input(promt)
    while bool(pattern.match(txt)):
        



import re

re_check = re.compile("^[a-z]*[-+]{0,1}\d*.{0,1}\d*[a-z]*$")
text = validator(re_check, ("Input text with digitals: "))
re_change = re.sub(r"[-+]{0,1}\d*.{0,1}\d*", "", text)
print(re_change)
#re_ckkf = re.sub()
# text = next_validator(re_slice, )
