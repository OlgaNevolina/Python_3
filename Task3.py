#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*

#- [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

my_list = [1.1, 1.2, 3.1, 5.567, 10.003]
new_lst = [round(i%1,3) for i in my_list if i%1 != 0]
print(max(new_lst) - min(new_lst))
