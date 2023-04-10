# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите длинну шоколадки: ')
long_choc = int(input())
print('Введите ширину шоколадки: ')
width_choc = int(input())
print('Введите необходимое количество долек: ')
quant_choc = int(input())

if quant_choc < long_choc * width_choc:
    if quant_choc % long_choc == 0 or quant_choc % width_choc == 0:
        print (f"Можно отломить {quant_choc} ")
    else:
        print (f"Нельзя отломить {quant_choc} ")
else:
        print (f"Нельзя отломить {quant_choc} ")
