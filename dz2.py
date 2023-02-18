# Петя и Катя – брат и сестра.
#  Петя – студент, а Катя – школьница. 
#  Петя помогает Кате по математике.
#   Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#   а Катя должна их отгадать.
#    Для этого Петя делает две подсказки. 
#    Он называет сумму этих чисел S и их произведение P.
#     Помогите Кате отгадать задуманные Петей числа.

sum_number = int(input('Введите сумму: '))
product_number = int(input('Введите произведение: '))
if(sum_number == product_number):
    print(sum_number//2, product_number//2)
for i in range(sum_number-1):
    j = sum_number-i
    if(product_number==i*j):          
        print(f'i = {i}, j = {j}')
        break


