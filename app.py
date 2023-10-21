import os
def soma(num1:int,num2:int) -> int:
    return num1+num2

while True:
    print('''
                                    =========== CALCULADORA ===========
          
         
          1- SOMA
          2- SUBTRAÇÃO
          3- MULTIPLICAÇÃO
          4- DIVISÃO

          0- SAIR
          ''')


    op= int(input('\nDigite o número da operação que deseja: '))


    match op:


        case 1:
            num1= int(input('Digite o primeiro valor: '))
            num2= int(input('Digite o segundo valor: '))
            total= soma(num1,num2)

            print(f'\nA soma de {num1} + {num2}= {total}')
            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls')
        case 2:
            num1= int(input('Digite o primeiro valor: '))
            num2= int(input('Digite o segundo valor: '))
            subtracao = num1 - num2
            print(f'\nA Subtração de {num1} - {num2}= {subtracao}')
            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls')
        case 3:
            num1= int(input('Digite o primeiro valor: '))
            num2= int(input('Digite o segundo valor: '))
            mult = num1 * num2
            print(f'\nA Multiplicação de {num1} X {num2}= {mult}')
            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls')
        case 4:
            num1= int(input('Digite o primeiro valor: '))
            num2= int(input('Digite o segundo valor: '))
            divisao = num1 / num2
            print(f'\nA Divisão de {num1} / {num2}= {divisao}')
            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls')