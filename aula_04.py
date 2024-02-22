# 22 DE FEVEREIRO DE 2024 - AULA 04 - PROGRAMAÇÃO EM PYTHON

# Modelo
# text = "Hi there!"
# name = input('Digite seu nome: ')
# print('{}{}'.format(text,name))
# print(f'Text {text}{name}')
# print("Texto" + text + name)
# print(text, name)

# Exercícios

# 1 - concatene uma cidade e um adjetivo para ela
# cidade = input('Digite o nome de uma cidade:')
# adjetivo = input('Digite um adjetivo:')
# print('{} {}'.format(cidade, adjetivo))

# 2 - concatene uma viagem e quem vai participar dela
# viagem = input('Digite para onde voce quer ir:')
# pessoas = input('Digite o número de passagens:')
# print('{} {}'.format(viagem, pessoas))

# 3 - concatene função programador seu nome ou o nome do usuário
# nome = 'James'
# funcao = 'Programador'
# nome_usuario = 'JJdr'
# print(nome, funcao, nome_usuario)

# Exercícios

# 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

# numero = 7
# expo = 7*2
# print(numero, expo)

# 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

# nome1 = input('Qual é o seu nome?')
# nome2 = input('E o seu sobrenome?')
# print('{} {}'.format(nome1, nome2))

# 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

# number1 = input('Escolha um número inteiro:')
# number2 = input('Escolha outro número inteiro:')
# print(f'Os dois números são: {number1}; {number2}')

# 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

# v1 = 'Python'
# v2 = input("Escolha um número inteiro:")
# print(f'{v1} {v2}')

# 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado. 

# frase = 'A aula de hoje será'
# palavra = input('Escolha uma palavra:')
# print(f'{frase} {palavra}') 

#Desafio
#Crie um sistema de calculadora 
#concatenar as saídas
#SOMA | DIVISÃO | MULTIPLICAÇÃO | SUBSTRAÇÃO 
#UTILIZAR input() - print() -  +|-|/ |**|*|// 

a1 = float(input('Digite um número:'))
a2 = float(input('Digite outro número:'))
soma = a1 + a2
sub = a1 - a2
multi = a1 * a2
div1 = a1 / a2
div2 = a1 // a2
exp = a1 ** a2
print(f' soma = {a1} + {a2} = {soma}')
print(f' subtração = {a1} - {a2} = {sub}')
print(f' multiplicação = {a1} * {a2} = {multi}')
print(f' divisão1 = {a1} / {a2} = {div1}')
print(f' divisão2 = {a1} // {a2} = {div2}')
print(f' exponencial = {a1} ** {a2} = {exp}')