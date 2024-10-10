def calculate():
    operation = input('''
Por favor, digite a operação matemática que você gostaria de realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Por favor, insira o primeiro número: '))
    number_2 = int(input('Por favor, insira o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um número válido, execute o programa novamente.')
    again()

def again():
    calc_again = input('''
Quer calcular novamente?
Digite S para SIM ou N para NÃO:''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais.')
    else:
        again()

calculate()