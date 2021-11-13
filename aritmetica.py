num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))

def soma():
    return num1 + num2
def subtracao():
    return num1 - num2
def multiplicacao():
    return num1 * num2
def divisao():
    return num1 / num2
def potenciacao():
    return num1 ** num2

print('A soma de {} mais {} é: {}'.format(num1, num2, soma()))
print('A subtracao de {} menos {} é: {}'.format(num1, num2, subtracao()))
print('A multiplicação de {} por {} é igual a: {}'.format(num1, num2, multiplicacao()))
print('A divisão de {} por {} é: {}'.format(num1, num2, divisao()))
print('A potenciação de {} elevado a {} tem como resultado: {}'.format(num1, num2, potenciacao()))
