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

print('A soma de',num1,'mais', num2, 'é:',soma())
print('A subtracao de',num1,'menos',num2,'é:', subtracao())
print('A multiplicação de',num1,'por',num2,'é igual a:',multiplicacao())
print('A divisão de',num1,'por',num2,'é:',divisao())
print('A potenciação de',num1,'elevado a',num2,'tem como resultado:',potenciacao())