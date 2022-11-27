tuple_1 = (1, 3, 4, 4, 4)
tuple_2 = ("one", "two")
tuple_3 = (2, 3.545, "three")
z = (tuple_1[0], 9, tuple_1[-1])
print(z)
print(tuple_1)
print(tuple_2)
print(tuple_3)

print(tuple_1.count(4))  # возвращает кол-во элементов в tuple
print(type(tuple_1))
person_tuple = ('John', 'Smith', 1998)
first_name, last_name, year_of_birth = person_tuple  # извлечение(распоковка) данных
print(first_name, last_name, year_of_birth)

t1 = (1, 2, 3, 4, 4, 7, 8)
print(t1.index(4))  # вычисление индекса элемента

computer_tuple = ('laptop', 'huawei', 'intel core i5', '13 inches')
computer_type, model, processor, size = computer_tuple
print(computer_type, model, processor, size)
