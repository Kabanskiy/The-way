# Напишите программу, которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.


a = ['baobab', 'bazuka', 10]
b = a
d = dict(zip(a, b))
print(d)

