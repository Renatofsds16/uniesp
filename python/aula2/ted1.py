"""
Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o
aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).
""" 

notas = [float(input(f'Digite a {i+1} nota: ')) for i in range(5)]
print('aprovado') if sum(notas)/len(notas) >= 7  else print('reprovado')



"""
Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário.
"""

def fatorial(numero:int) -> int:
    return numero * (numero + 1) / 2

    
print(fatorial(3))


"""
Crie uma função que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
desconsiderando espaços e pontuação).
"""


def eh_palindromo():
    frase = input("Digite uma palavra para ver se e um palíndromo: ").lower().replace(' ','')
    if frase == frase[::-1]:
        print("E um palindromo")
    else:
        print('NAO e um palindromo')
    

eh_palindromo()



"""
Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.
"""

numero = input("digite um numero: ")
if numero.isdigit():
    lista_numeros = [int(n) for n in numero]
    print(sum(lista_numeros))


"""Crie uma função que verifica se um número é primo ou não."""
def eh_primo(numero:int):
    if numero <= 1:
        print("Nao e primo")
    for i in range(2,numero):
        if numero % i == 0:
            print("Nao e primo")
            return
    print("E primo")

eh_primo(9)



"""
Escreva um programa que recebe uma string e conta a quantidade de vogais 
(a, e, i, o, u) presentes
nela.""" 

string = input("Digite uma palavra: ")
c = 0
for i in string:
    if i in ('aeiou'):
        c+=1
print(c)
 

"""
Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura
e peso.
"""

def calc_imc(altura,peso):
    return peso / (altura * altura)

altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
print(f'O imc e de: {calc_imc(altura,peso):.2f}')



"""
Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa,
dependendo da escolha do usuário.
"""

def to_convert(temperatura,conversor):
    if conversor == 'c':
        valor = (temperatura * 9/5) + 32
        print(f'{temperatura} Celsius em Fahrenheit e {valor:.2f}')
    else:
        valor = (temperatura - 32 ) * 5 / 9
        print(f'{temperatura} Fahrenheit em Celsius e {valor:.2f}')


temperatura = float(input('Digite a temperatura: '))
conversor = input('Digite c para Celsius ou f para Fahrenheit: ').lower()
to_convert(temperatura,conversor)


"""
Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base
na escolha do usuário.
"""

def calculadora(a,b,operacao):
    match operacao:
          case '+': return a + b
          case '-': return a - b
          case '*': return a * b
          case '/':
            if b == 0:
                return "nao e possivel dividir por 0"


n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
operacao = input('digite + - * / para calcular: ')
print(calculadora(n1,n2,operacao))


"""
Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos
especificado pelo usuário.

"""
def seq_fibonacci(numero):
    if numero < 0:
        return []
    if numero == 1:
        return [0]
    seq = [0,1]
    for i in range(2,numero):
        n = seq[-1] + seq[-2]
        seq.append(n)
    return seq

termos = int(input('digite numero de termos: '))
print(seq_fibonacci(termos))
        