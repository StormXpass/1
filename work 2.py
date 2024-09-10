numbers = []
while True:
    user_input = input("Введите число (или 'stop' для завершения): ")
    if user_input.lower() == 'stop':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Это не число, попробуйте снова.")
print("Введённые числа:", numbers)


#list = [8, 4, 7, 1, 9, 3, 15]
#print(list)
#list.append(12)
#print(list)

#for item in list:
    #print(item * 2, end=' ')


#for i in range(10):
    #print("Hello!")